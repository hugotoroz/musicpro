from django.urls import path

from . import views
from api.views import consultar_producto

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('consultar_producto/<slug:slug>/', consultar_producto, name='consultar_producto'),
]