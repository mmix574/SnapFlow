from django.contrib import admin

# Register your models here.


# start coding here
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from  .models import UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


from message.models import MessageStatus
class MessageStatusInline(admin.StackedInline):
    model = MessageStatus
    max_num = 1

    can_delete = False
    verbose_name = 'message'

class UserprofileAdmin(UserAdmin):
    inlines = [ProfileInline,MessageStatusInline,]



admin.site.unregister(User)
admin.site.register(User,UserprofileAdmin)

# admin.site.register(User,MessageStatusInline)