from django.http import JsonResponse
from store.models import Product, Category
from django.contrib.auth.models import User


def consultar_producto(request, slug):
    try:
        producto = Product.objects.get(slug=slug)
        return JsonResponse(
            {
                'nombre': producto.name, 
                'marca': producto.brand, 
                'descripcion': producto.description, 
                'precio': str(producto.price), 
                'stock': producto.in_stock
            })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'})


def consultar_categoria(request, slug):
    try:
        categoria = Category.objects.get(slug=slug)
        return JsonResponse(
            {'nombre': categoria.name, 'slug': categoria.slug})
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Categoría no encontrada'})


def consultar_usuario(request, user):
    try:
        usuario = User.objects.get(username=user)
        return JsonResponse({'username': usuario.username, 'email': usuario.email})
    except User.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'})
