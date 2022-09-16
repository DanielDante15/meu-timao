from django.shortcuts import render, HttpResponseRedirect

from .models import Produto

def home_tela(request):
    produtos = Produto.objects.all()
    
    dados = {
        'produtos':produtos
    }

    return render(request,'index.html',dados)



def entrar(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/admin/login/?next=/admin/')

def sair(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/admin/logout')