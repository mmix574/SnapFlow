from django.contrib import admin

# Register your models here.


from .models import SystemToUserMessage
from .models import MessageStatus
from .models import UserToUserMessage
from .models import EventMessage
from .models import Friend


class SystemToUserMessageAdmin(admin.ModelAdmin):
    list_display = ['user','tittle','time']




admin.site.register(SystemToUserMessage,SystemToUserMessageAdmin)

admin.site.register(MessageStatus)


class UserToUserMessageAdmin(admin.ModelAdmin):
    list_display = ['a_user','b_user','content']

admin.site.register(UserToUserMessage,UserToUserMessageAdmin)


class EventMessageAdmin(admin.ModelAdmin):
    list_display = ['user','event_type','brief_content','time']

admin.site.register(EventMessage,EventMessageAdmin)



class FriendAdmin(admin.ModelAdmin):
    list_display = ['user','has_friend']
    search_fields = ['user']
admin.site.register(Friend,FriendAdmin)


from .models import UserToUserMessageSession
class UserToUserMessageSessionAdmin(admin.ModelAdmin):
    list_display = ['a_user','b_user','time']
admin.site.register(UserToUserMessageSession,UserToUserMessageSessionAdmin)