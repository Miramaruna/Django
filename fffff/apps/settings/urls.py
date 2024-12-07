from django.urls import path
from apps.settings.views import settings

urlpatterns = [
    path('', settings, name='setting')
]