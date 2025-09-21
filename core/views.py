from django.shortcuts import render
from .models import Pessoa

def listar_pessoas(request):
    pessoas = Pessoa.objects.select_related('usuario').prefetch_related('endereco_set')
    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'index.html', contexto)