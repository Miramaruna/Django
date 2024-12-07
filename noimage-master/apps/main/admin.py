from django.contrib import admin
from apps.main.models import Main
# Register your models here.

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'logo', 'facebook', 'instagram', 'youtube']
    
