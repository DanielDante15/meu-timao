from django.shortcuts import render

def home_tela(request):
    return render(request,'index.html')
