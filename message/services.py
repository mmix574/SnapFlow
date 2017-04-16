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