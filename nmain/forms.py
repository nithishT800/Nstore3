from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import customer
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['name', 'email', 'mobile']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Enter the name...'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email...'}),
                   'mobile': forms.TextInput(attrs={'placeholder': 'Mobile...'})}
