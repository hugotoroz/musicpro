from django.db import models
# Permisos de cada usuario.
class Permiso(models.Model):
    id_permiso = models.BigAutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=100)
    pass
# Roles de cada usuario.
class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    id_permiso = models.ForeignKey(Permiso)
    pass
# Los usuarios del sistema se dividirán por roles para saber si es cliente, vendedor, administrador, etc.
class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.IntegerField()
    id_rol = models.ForeignKey(Rol)
