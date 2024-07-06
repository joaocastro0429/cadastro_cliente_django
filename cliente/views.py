from django.shortcuts import render
# from django.http  import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView , ListView,UpdateView,DetailView,DeleteView
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

class clienteDetailView(DetailView):
    model=Cliente
    template_name="list_detail.html"
    # renomeano o nome da variavel
    context_object_name="cliente"



class clienteListUpdateView(UpdateView):
    model=Cliente
    fields=("nome","profissao","data_nascimento")
    template_name="form_clientes.html"
    # direcionando para a listagem 
    success_url=reverse_lazy("lista_clientes")


class clienteDeleteView(DeleteView):
    model=Cliente
    template_name="remover_clientes.html"
    success_url=reverse_lazy("lista_clientes")
    