from django.core.management.base import BaseCommand,CommandError



from django.contrib.auth.models import User

from message.models import MessageStatus

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        users = User.objects.all()
        for i in users:
            MessageStatus.objects.get_or_create(user=i)
            pass
        pass

