from core.models import Usuario, Rol, Permiso
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer, RolesSerializer, PermisosSerializer
from rest_framework import viewsets, permissions
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= UsuarioSerializer
class RolViewSet(viewsets.ModelViewSet):
    queryset= Rol.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= RolesSerializer
class PermisoViewSet(viewsets.ModelViewSet):
    queryset= Permiso.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= PermisosSerializer