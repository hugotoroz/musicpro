from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import UsuarioSerializer,RolesSerializer,PermisosSerializer
from core.models import Usuario,Rol,Permiso
# Create your views here.

@csrf_exempt

def index(request):

    return render(request,'index.html')

@api_view(['GET','POST'])
def lista_usuarios(request):
    if request.method == 'GET':
        mascotas = Usuario.objects.all()
        serializer = UsuarioSerializer(mascotas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def lista_roles(request):
    if request.method == 'GET':
        mascotas = Rol.objects.all()
        serializer = RolesSerializer(mascotas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = RolesSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def lista_permisos(request):
    if request.method == 'GET':
        mascotas = Permiso.objects.all()
        serializer = PermisosSerializer(mascotas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = PermisosSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    