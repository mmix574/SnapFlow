from django.core.management.base import BaseCommand,CommandError

from forum.models import Thread
class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        ts = Thread.objects.all()
        for i in ts:
            print(i)
            i.score = i.reply *200+i.like*100+i.view*20
            i.save()
        pass

