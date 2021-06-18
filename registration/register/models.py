from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta : 
        abstract = True



class Profil(Base):
    user = models.OneToOneField(User, related_name="userdjango", on_delete=models.CASCADE)
    prenom = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"




