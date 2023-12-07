from typing import Any
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import Ropa,ImplementosDeportivos

# Create your views here.
class RopaListView(ListView):
    template_name='Ropa.html'
    queryset = Ropa.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de producto'
        
        print(context)
        return context

        


class ImplementosDeportivosListView(ListView):
    template_name='implementosdeportivos.html'
    queryset = ImplementosDeportivos.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de producto'
        
        print(context)
        return context


class ImplementosDeportivosDetailView(DetailView):
    model = ImplementosDeportivos
    template_name = 'inventario/DeportivoVista.html'