from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_vagas, name='listar_vagas'),
]
