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

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': 'form-control',
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your email",
        'class': 'form-control',
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your password",
        'class': 'form-control',
        'type': 'password',
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Repeat password",
        'class': 'form-control',
        'type': 'password',
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already been registered.")
        return email

