from django.db import models

class Vaga(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('fechada', 'Fechada'),
    ]

    titulo = models.CharField(max_length=200)
    setor = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberta')
    data_abertura = models.DateField()

    def __str__(self):
        return self.titulo
