from django.shortcuts import render
# from django.http  import HttpResponse
from django.views.generic import CreateView , ListView,UpdateView
from .models import Cliente
# Create your views here.
class clienteCreateView(CreateView):
    model=Cliente
    fields='__all__'
    template_name="form_clientes.html"
    success_url="lista_clientes"


class clienteListView(ListView):
    model=Cliente
    template_name="list_clientes.html"

class clienteListUpdateView(UpdateView):
    model=Cliente
    fields=("nome","profissao","data_nascimento")
    template_name="form_clientes.html"