from django.contrib import admin
from django.urls import path

def desdeApps(self):
    print('=================DESDE LA APP DEPARTAMENTO===================')

urlpatterns = [
    path('departamento/', desdeApps)
]
