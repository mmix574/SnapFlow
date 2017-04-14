from django.core.management.base import BaseCommand,CommandError
from django.contrib.auth.models import User
import random


from django.contrib.auth.models import User
from index.models import UserProfile

def get_random_username():
    start_with = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@/./+/-/_"
    sa = []
    sa.append(random.choice(start_with))
    for i in range(7):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

class Command(BaseCommand):
    help = 'what the fuck you are doing?'
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)


    def handle(self, *args, **options):
        print("creating fake users")
        # print(User.objects.all())

        _name = get_random_username()

        #
        u = User()
        u.username = _name
        u.email = _name+"@gmail.com"
        u.save()

        #
        # create_user = User.objects.filter(username=_name)
        # if not create_user:
        #     return

        # user = create_user[0]
        u.userprofile.language = "english"
        u.work_place = "google"
        u.userprofile.work_nickname = "hacker-painter"
        u.userprofile.self_introduction = "もしも彼らが君の何かを盗んだとして それはくだらないものだよ  返して贳うまでもない筈甚至何故なら価値は生命に従って付いている"

        u.userprofile.avatar="ava/2_4ydFf85.jpg"

        u.userprofile.save()