from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_candidatos, name='listar_candidatos'),
    path('candidaturas/', views.listar_candidaturas, name='listar_candidaturas'),
]
