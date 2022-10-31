from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_tela, name='home_tela'),
    path("entrar", views.entrar, name='entrar'),
    path("sair", views.sair, name='sair'),
    path("login", views.login, name='login'),
]
