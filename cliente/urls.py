from django.urls import path
from .views import clienteCreateView,clienteListView,clienteListUpdateView,clienteDetailView,clienteDeleteView

urlpatterns = [
    path("form_cliente",clienteCreateView.as_view() ),
    path("lista_clientes",clienteListView.as_view(), name="lista_clientes"),
    path("form_cliente/<int:pk>",clienteListUpdateView.as_view(), name="editar_cliente"),
    path("lista_cliente/<int:pk>",clienteDetailView.as_view(),name="lista_cliente"),
    path("remover_cliente/<int:pk>",clienteDeleteView.as_view() , name="remover_cliente")

]