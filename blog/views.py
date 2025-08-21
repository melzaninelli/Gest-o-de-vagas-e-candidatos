from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, mundo! Bem-vindo ao meu primeiro projeto Django 🚀")
