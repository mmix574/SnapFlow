from django.core.management.base import BaseCommand,CommandError

import random
from django.contrib.auth.models import User
from index.models import UserProfile
class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        work_nickname = ["算法工程师","JAVA工程师","C++工程师","Python WEB","博士顾问","产品经理"]
        work_place = ["腾讯IEG","腾讯","Google","Facebook","微软亚洲研究院","山东华为","摩拜","ofo","滴滴出行","美团外卖","腾讯SNG","腾讯WXG","蘑菇街","百度"]
        self_introduction = ["天才是百分之九十九的汗水加百分之一灵感。","从哪里跌倒，从哪里爬起。","有志者事竟成。","人生的道路不会一帆风顺，事业的征途也充满崎岖艰险，只有奋斗，只有拼搏，才会达到成功的彼岸。","少壮不努力，老大徒伤悲。"]



        profiles = UserProfile.objects.all()

        for i in profiles:
            print(i)
            i.work_nickname = random.choice(work_nickname)
            i.work_place = random.choice(work_place)
            i.self_introduction = random.choice(self_introduction)
            i.save()
