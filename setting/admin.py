from django.contrib import admin

# Register your models here.


from .models import SystemEmailInfo
from .models import WelcomeSystemMessage


class WelcomeSystemMessageAdmin(admin.ModelAdmin):
    list_display = ['tittle','content']


admin.site.register(SystemEmailInfo)
admin.site.register(WelcomeSystemMessage,WelcomeSystemMessageAdmin)