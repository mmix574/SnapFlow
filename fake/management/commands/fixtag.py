from django.core.management.base import BaseCommand,CommandError

from forum.models import Thread
from forum.models import TAG

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        import jieba.posseg as pseg
        accept_type = ['v', 'n', 'f', 'ns', 'a', 'eng', 't', 'nr', 'l', 'vn', 'nz', 'b', 'b', 's', 'j', 'nt', 'an',
                       'z', 'nrt']
        threads = Thread.objects.all()
        for t in threads:
            s = t.tittle
            if not s:
                continue
            else:
                words = pseg.cut(s)
                for word, flag in words:
                    if flag in accept_type:
                        tag = TAG()
                        tag.thread = t
                        tag.name = word
                        tag.save()
