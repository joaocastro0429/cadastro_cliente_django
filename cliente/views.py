from django.shortcuts import render
# from django.http  import HttpResponse
from django.views.generic import CreateView
from .models import Cliente
# Create your views here.
class clienteCreateView(CreateView):
    model=Cliente
    fields='__all__'
    template_name="form_clientes.html"


