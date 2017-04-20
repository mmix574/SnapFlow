from django.contrib import admin

# Register your models here.


from . import models

class CreditStatusAdmin(admin.ModelAdmin):
    list_display = ['user','credit_point']

admin.site.register(models.CreditStatus,CreditStatusAdmin)



admin.site.register(models.UserCreditNickName)
admin.site.register(models.CashPoint)



class CreditExchangeCodeAdmin(admin.ModelAdmin):
    list_display = ['code','point']
admin.site.register(models.CreditExchangeCode,CreditExchangeCodeAdmin)



admin.site.register(models.CreditLog)