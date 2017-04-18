from django.contrib import admin

# Register your models here.


from .models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user','type','brief_content','create_time']

admin.site.register(History,HistoryAdmin)