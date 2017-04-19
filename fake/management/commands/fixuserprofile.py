from django.core.management.base import BaseCommand,CommandError



from django.contrib.auth.models import User
from index.models import UserProfile
class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        work_nickname = "算法工程师"
        work_place = "腾讯IEG"
        self_introduction = "哪里有天才，我是把别人喝咖啡的工夫都用在了工作上了。"



        profiles = UserProfile.objects.all()

        for i in profiles:
            print(i)
            i.work_nickname = work_nickname
            i.work_place = work_place
            i.self_introduction = self_introduction
            i.save()
