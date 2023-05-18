from django.db import models

# Create your models here.
class Permiso(models.Model):
    id_permiso = models.BigAutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_permiso


class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=30)
    fk_id_permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE,)

    def __str__(self):
        return self.nombre_rol


class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True)
    comuna = models.CharField(max_length=45)

    def __str__(self):
        return self.comuna


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    celular = models.IntegerField()
    correo = models.CharField(max_length=200)
    #
    #CAMPO CLAVE BORRADO
    #
    direccion = models.CharField(max_length=100)
    fk_id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE,)
    fk_id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,)

    def __str__(self):
        return self.correo

