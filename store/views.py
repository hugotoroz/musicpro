from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from api.views import consultar_producto
import json


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    respuesta = consultar_producto(request,slug)
    print(respuesta)
    json_data = json.loads(respuesta.content)
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context= { 'product':product, 'api':json_data }   
    """
    #RESPUESTA EN JSON
    response = render(request, 'store/products/detail.html', context)
    response['Content-Type'] = 'application/json'
    response.content = json.dumps(json_data)
    
    return response
    """
    
    return render(request, 'store/products/detail.html', context)
    
    
    
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 
                                                            'products':products})
    