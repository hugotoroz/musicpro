from django.urls import path
from .views import index, lista_permisos, lista_roles, lista_usuarios

urlpatterns = [
    path('', index, name="index"),
    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('lista_roles/', lista_roles, name="lista_roles"),
    path('lista_permisos/', lista_permisos, name="lista_permisos"),
]
