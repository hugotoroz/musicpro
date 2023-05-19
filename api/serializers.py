from rest_framework import serializers
from core.models import Usuario, Rol, Permiso
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre_usuario','apellido_usuario','celular','correo','direccion','fk_id_rol','fk_id_comuna']
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
        



