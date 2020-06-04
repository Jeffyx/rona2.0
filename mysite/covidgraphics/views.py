from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date, datetime, timedelta
import json
import re

def getData():
    currentDate = date(2020, 3, 18) 
    delta = timedelta(days=1)
    end_date = date.today() - delta
    
    covidList = []

    while currentDate < end_date:
        currentDate += delta
        responsePA = requests.get("https://covidtracking.com/api/states/daily?state=PA&date=" + currentDate.strftime('%Y%m%d'))
        covidList.append(responsePA.json())     
    
    newList = []
    for day_dict in covidList:
        new_dict = {}
        keys = list(day_dict.keys())
        values = list(day_dict.values())
        for i in range(0, len(day_dict)):
            new_key = str(keys[i])
            new_key = new_key[0].upper() + new_key[1:]
            new_key = re.sub(r"(\w)([A-Z])", r"\1 \2", new_key)
            dict_item = {new_key: values[i]}
            new_dict.update(dict_item)
        newList.append(new_dict)
    
    return newList

def chartDeaths(request):
    newList = getData()
    return render(request, 'deaths.html', context={"covidDict": newList})
    
def chartHospitalizations(request):
    newList = getData()
    return render(request, 'hospitalizations.html', context={"covidDict": newList})

def chartVentilators(request):
    newList = getData()
    return render(request, 'ventilators.html', context={"covidDict": newList})
