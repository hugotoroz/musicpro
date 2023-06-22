from rest_framework import serializers
from core.models import Usuario, Rol, Permiso
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','last_login','date_joined']
        read_only_fields = ('id_usuario',)

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol','nombre_rol','fk_id_permiso']
        read_only_fields = ('id_rol',)

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ['id_permiso','nombre_permiso']
        read_only_fields = ('id_permiso',)
        



