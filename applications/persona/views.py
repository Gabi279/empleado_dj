from django.shortcuts import render

from django.views.generic import (
    ListView,
    ) 

from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado

# Create your views here.
