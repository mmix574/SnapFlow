from django.contrib import admin

# Register your models here.
from .models import Class
from .models import SubClass


admin.site.register(Class)
admin.site.register(SubClass)