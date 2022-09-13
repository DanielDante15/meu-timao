from django.shortcuts import render

from .models import Produto

def home_tela(request):
    produtos = Produto.objects.all()
    
    dados = {
        'produtos':produtos
    }

    return render(request,'index.html',dados)
