from django.core.management.base import BaseCommand,CommandError

from forum.models import Comment

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        comments = Comment.objects.all()
        for i in comments:
            if i.content.strip()=="":
                print(i.id)
                i.delete()
