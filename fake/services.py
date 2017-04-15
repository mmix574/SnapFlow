from django.contrib.auth.models import User
import random


def ramdom_user():
    users = User.objects.all()
    if users:
        return random.choice(users)
    return None
