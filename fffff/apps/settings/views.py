from django.shortcuts import render
from apps.settings.models import Basesettings, Employees, Blog
# Create your views here.

def settings(request):
    setting = Basesettings.objects.latest('id')
    employe = Employees.objects.all()
    blog = Blog.objects.all().order_by("?")[:3]
    return render(request, 'index.html', locals())
