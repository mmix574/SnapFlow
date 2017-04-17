from django.core.management.base import BaseCommand,CommandError

from forum.models import Comment

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        comments = Comment.objects.filter(content=" \r")
        print(len(comments))
        for i in comments:
            i.delete()