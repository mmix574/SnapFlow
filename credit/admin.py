from django.contrib import admin

# Register your models here.


from . import models


admin.site.register(models.UserCreditDefault)
admin.site.register(models.UserCreditNickName)
admin.site.register(models.CashPoint)