from django.contrib import admin

# Register your models here.


from . import models


admin.site.register(models.CreditDefault)
admin.site.register(models.UserCreditNickName)
admin.site.register(models.CashPoint)