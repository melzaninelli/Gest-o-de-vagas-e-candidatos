from django.db import models
from vagas.models import Vaga

class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    e_mail = models.EmailField()
    data_nascimento = models.DateField()
    experiencia = models.TextField()

    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    STATUS_CANDIDATURA = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
    ]

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data = models.DateField()
    status_candidatura = models.CharField(max_length=10, choices=STATUS_CANDIDATURA, default='pendente')

    def __str__(self):
        return f"{self.candidato.nome} -> {self.vaga.titulo} ({self.status_candidatura})"
