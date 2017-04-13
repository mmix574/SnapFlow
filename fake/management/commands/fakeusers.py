from django.core.management.base import BaseCommand,CommandError
from django.contrib.auth.models import User
import random


def get_random_username():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@/./+/-/_"
    sa = []
    for i in range(8):
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
        # u = User()
        print(get_random_username())