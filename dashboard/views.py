from django.shortcuts import render
from vagas.models import Vaga
from candidatos.models import Candidato, Candidatura
import pandas as pd
from datetime import date

def dashboard(request):
    # transformar dados em DataFrames
    vagas = pd.DataFrame(list(Vaga.objects.all().values()))
    candidatos = pd.DataFrame(list(Candidato.objects.all().values()))
    candidaturas = pd.DataFrame(list(Candidatura.objects.all().values()))

    context = {}

    if not vagas.empty:
        # Total de vagas abertas e fechadas
        context['vagas_abertas'] = vagas[vagas['status'] == 'aberta'].shape[0]
        context['vagas_fechadas'] = vagas[vagas['status'] == 'fechada'].shape[0]

        # Setor com mais vagas abertas
        setor_vagas = vagas[vagas['status'] == 'aberta'].groupby('setor').size()
        context['setor_mais_vagas'] = setor_vagas.idxmax() if not setor_vagas.empty else "Nenhum"

    if not candidatos.empty:
        # Média de idade dos candidatos
        hoje = date.today()
        candidatos['idade'] = candidatos['data_nascimento'].apply(lambda d: hoje.year - d.year - ((hoje.month, hoje.day) < (d.month, d.day)))
        context['media_idade'] = round(candidatos['idade'].mean(), 2)

    if not candidaturas.empty:
        # Número de candidatos por vaga
        num_candidatos_vaga = candidaturas.groupby('vaga_id').size().to_dict()
        context['num_candidatos_vaga'] = num_candidatos_vaga

    return render(request, 'dashboard/dashboard.html', context)
