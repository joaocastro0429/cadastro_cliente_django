from django.urls import path
from .views import clienteCreateView,clienteListView

urlpatterns = [
    path("form_cliente",clienteCreateView.as_view() ),
    path("lista_clientes",clienteListView.as_view(), name="lista_clientes"),
    

]