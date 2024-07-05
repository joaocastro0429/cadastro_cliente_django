from django.urls import path
from .views import clienteCreateView,clienteListView,clienteListUpdateView

urlpatterns = [
    path("form_cliente",clienteCreateView.as_view() ),
    path("lista_clientes",clienteListView.as_view(), name="lista_clientes"),
    path("form_cliente/<int:pk>",clienteListUpdateView.as_view())

]