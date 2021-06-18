from django.contrib import admin
from .models import Profil
# Register your models here.

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'prenom', 'phone', 'date_add')
    search_fields = ('user',)