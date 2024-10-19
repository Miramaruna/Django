from django.urls import path
from apps.main.views import main

urlpatterns = [
    path('', main, name='main'),
]