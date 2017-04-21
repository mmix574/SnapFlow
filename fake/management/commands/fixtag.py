from django.core.management.base import BaseCommand,CommandError

from forum.models import Thread
from forum.models import TAG

class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        import jieba.posseg as pseg
        # accept_type = ['v', 'n', 'f', 'ns', 'a', 'eng', 't', 'nr', 'l', 'vn', 'nz', 'b', 'b', 's', 'j', 'nt', 'an','z', 'nrt']
        accept_type = ['n','ns','eng','nr','l','vn','nz','s','j','nt','nrt']
        threads = Thread.objects.all()
        j = 1
        for t in threads:
            s = t.tittle
            print(j,s)
            words = pseg.cut(s)
            for word, flag in words:
                if flag in accept_type:
                    tag = TAG()
                    tag.thread = t
                    tag.name = word[:30]
                    tag.save()
            j = j+1

        # tags = TAG.objects.all()
        # j = 1
        # for i in tags:
        #     print(j,i.name)
        #     j=j+1
        #     i.delete()