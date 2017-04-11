from django.core.management.base import BaseCommand,CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'what the fuck you are doing?'
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)


    def handle(self, *args, **options):
        print("creating fake users")
        print(User.objects.all())
