from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import models
from django.core.validators import validate_email

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get('nom')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("register")
        else:
            print("error")
    return render(request, "index.html", locals())

def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False

def register(request):

    if request.method == 'POST':
        username = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = User.objects.create_user(username=username ,email=email ,password=password1)
        user.save()
        profil = models.Profil(prenom=prenom,phone=phone, user=user)
        profil.save()

        return redirect("index")
        
    return render(request, "inscription.html", locals())




