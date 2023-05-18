from rest_framework import serializers
from core.models import Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre_usuario','apellido_usuario','celular','correo','direccion','fk_id_rol','fk_id_comuna']

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_rol','nombre_rol','fk_id_permiso']
class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_permiso','nombre_permiso']
        



