from django.contrib import admin

# Register your models here.
from .models import Class
from .models import SubClass

from .models import Thread


admin.site.register(Class)
admin.site.register(SubClass)
# admin.site.register(Thread)