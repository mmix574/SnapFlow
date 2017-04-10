from django.contrib import admin

# Register your models here.


from .models import SystemToUserMessage

admin.site.register(SystemToUserMessage)