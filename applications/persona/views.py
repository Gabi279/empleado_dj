from re import template
from tempfile import tempdir
from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )

from applications.departamento.models import Departamento 

from .models import Empleado

class InicioView(TemplateView):
    """ vista que cargue la pagina de inicio """
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
        
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista
    
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('******************')
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado: ', lista)
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        return empleado.habilidades.all()
    
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"

    
class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
   
    
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***************METODO POST**********************')
        print('=======================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print('***************METODO form valid**********************')
        print('********************************')
        return super(EmpleadoUpdateView , self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado

    success_url = reverse_lazy('persona_app:correcto')