from django.core.management.base import BaseCommand,CommandError


from forum.models import Thread

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        # print("Template Command Calling...")
        i = Thread.objects.all()[0]
        print(i)
        pass

