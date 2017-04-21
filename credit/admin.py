from django.contrib import admin

# Register your models here.


from . import models

class CreditStatusAdmin(admin.ModelAdmin):
    list_display = ['user','credit_point']
admin.site.register(models.CreditStatus,CreditStatusAdmin)





class CreditExchangeCodeAdmin(admin.ModelAdmin):
    list_display = ['code','point']
admin.site.register(models.CreditExchangeCode,CreditExchangeCodeAdmin)


class CreditLogAdmin(admin.ModelAdmin):
    list_display = ['user','brief_content','time']
admin.site.register(models.CreditLog,CreditLogAdmin)



admin.site.register(models.UserCreditNickName)
admin.site.register(models.CashPoint)

class EverydaySignAdmin(admin.ModelAdmin):
    list_display = ['user','time']

admin.site.register(models.EverydaySign,EverydaySignAdmin)

class OnlineLogAdmin(admin.ModelAdmin):
    list_display = ['user','time']
admin.site.register(models.OnlineLog,OnlineLogAdmin)