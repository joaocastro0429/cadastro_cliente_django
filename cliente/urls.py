from django.urls import path
from .views import clienteCreateView

urlpatterns = [
    path("form_cliente",clienteCreateView.as_view() )
]