from django.urls import path

from . import views

urlpatterns = [
    path('deaths', views.chartDeaths, name='chartDeaths'),
    path('hospitalizations', views.chartHospitalizations, name='chartHospitalizations'),
    path('ventilators', views.chartVentilators, name='chartVentilators'),
]
