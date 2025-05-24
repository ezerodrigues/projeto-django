from django.http import HttpResponse
# from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>Página Inicial Django</h1>')

def sobre(request):
    return HttpResponse ('<h2>Sobre</h2>')

def contato(request):
    return HttpResponse ('<h2>Contato</h2>')
