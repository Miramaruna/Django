from django.contrib import admin
from apps.settings.models import Basesettings, Employees, Blog
# Register your models here.

admin.site.register(Basesettings)
admin.site.register(Employees)
admin.site.register(Blog)