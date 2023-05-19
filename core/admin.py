from django.contrib import admin

from .models import Comuna,Permiso,Rol,Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Permiso)
admin.site.register(Comuna)
