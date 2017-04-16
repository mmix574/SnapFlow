from django.contrib import admin

# Register your models here.


from .models import AdminBroadCast



class AdminBroadCastAdmin(admin.ModelAdmin):
    list_display = ['tittle',"create_time"]

admin.site.register(AdminBroadCast,AdminBroadCastAdmin)