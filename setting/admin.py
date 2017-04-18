from django.contrib import admin

# Register your models here.


from .models import SystemEmailInfo
from .models import WelcomeSystemMessage

admin.site.register(SystemEmailInfo)
admin.site.register(WelcomeSystemMessage)