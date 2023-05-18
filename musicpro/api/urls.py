from django.urls import path
from rest_framework import routers
from .api import UsuarioViewSet,RolViewSet,PermisoViewSet
router= routers.DefaultRouter()
router.register('lista_users',UsuarioViewSet,'lista_users')
router.register('lista_roles',RolViewSet,'lista_roles')
router.register('lista_permisos',PermisoViewSet,'lista_permisos')
urlpatterns = router.urls