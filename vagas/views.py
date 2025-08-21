from django.shortcuts import render
from .models import Vaga

def listar_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas/listar_vagas.html', {'vagas': vagas})

