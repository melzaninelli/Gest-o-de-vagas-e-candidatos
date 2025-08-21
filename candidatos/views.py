from django.shortcuts import render
from .models import Candidato, Candidatura

def listar_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'candidatos/listar_candidatos.html', {'candidatos': candidatos})

def listar_candidaturas(request):
    candidaturas = Candidatura.objects.select_related('candidato', 'vaga')
    return render(request, 'candidatos/listar_candidaturas.html', {'candidaturas': candidaturas})
