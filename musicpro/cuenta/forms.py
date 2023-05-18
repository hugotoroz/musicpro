from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your password",
        'class': 'form-control',
        'type': 'password',
    }))    