from django.core.management.base import BaseCommand,CommandError


from forum.models import Comment

from datetime import datetime
from datetime import timedelta

from django.utils import timezone

import random
class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        # print("Template Command Calling...")
        threads = Comment.objects.all()
        for i in threads:
            print(i,i.create_time)
            time_shift = random.randint(0,43200)
            i.create_time = i.thread.create_time+timedelta(seconds=time_shift)
            print("-->",i.create_time)
            i.save()


