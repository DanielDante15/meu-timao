from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_tela, name='home_tela') 
]
