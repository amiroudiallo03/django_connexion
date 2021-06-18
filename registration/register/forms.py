from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . import models



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class profilform(ModelForm):
    class Meta:
        model = models.Profil
        fields= ['prenom', 'phone']




