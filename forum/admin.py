from django.contrib import admin


from .models import Class
from .models import SubClass

class ClassAdmin(admin.ModelAdmin):
    pass
    list_display = ["name","create_time"]

    # name = models.CharField("hehe", max_length=20, blank=True, null=True)
    # chinese_name = models.CharField(max_length=20, blank=True, null=True)
    # create_user = models.ForeignKey(User, default=1, blank=True, null=True)
    # create_time

admin.site.register(SubClass)
admin.site.register(Class,ClassAdmin)
