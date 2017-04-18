from .models import UserMessageStatus

from django.contrib.auth.models import User


def get_user_to_user_message_count(uid):
    user = {}
    try:
        user = User.objects.get(id=uid)
    except:
        return None
    ums = UserMessageStatus.objects.get_or_create(user=user)


def get_system_to_user_message_count(uid):
    pass

def get_even_message_count(uid):
    pass





def send_system_message_to_all(message_tittle,message_content):
    from message.models import SystemToUserMessage
    from django.contrib.auth.models import User
    users = User.objects.all()
    print("正在发送系统消息","共有",len(users),"名用户","请耐心等待")
    for i in users:
        ms = SystemToUserMessage()
        ms.user = i
        ms.tittle = message_tittle
        ms.content = message_content
        ms.save()
    pass

def send_system_message_to_single_user(user,message_tittle,message_content):
    pass
