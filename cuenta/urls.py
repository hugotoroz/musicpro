from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm 


app_name = 'cuenta'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
    template_name='cuenta/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
]