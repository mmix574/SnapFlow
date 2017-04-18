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
admin.site.register(UserToUserMessage)
admin.site.register(EventMessage)



class FriendAdmin(admin.ModelAdmin):
    list_display = ['user','has_friend']
    search_fields = ['user']
admin.site.register(Friend,FriendAdmin)