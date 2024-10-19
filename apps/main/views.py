from django.shortcuts import render
from apps.main.models import Main
# Create your views here.

def main(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html', locals())

