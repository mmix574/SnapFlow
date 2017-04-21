from django.core.management.base import BaseCommand,CommandError
from forum.models import Thread,Comment,Class,SubClass
from fake.services import ramdom_user
import random

import json
class Command(BaseCommand):
    help = 'Command Line Template'
    main_class = "技术"
    sub_class = "程序员"

    filename = "programmer-1-50.json"

    main_class_instance = None
    sub_class_instance = None

    # 查找main_class_id 与sub_class_id
    def before_handle(self):
        if not Class.objects.filter(display_name=self.main_class):
            print("main_class not found")
            exit(1)
        if not SubClass.objects.filter(display_name=self.sub_class):
            print("sub_class not found")
            exit(2)

        self.main_class_instance = Class.objects.filter(display_name=self.main_class)[0]
        self.sub_class_instance = SubClass.objects.filter(display_name=self.sub_class)[0]
        print("before_handle ready")
        print("准备数据到"+self.main_class+","+self.sub_class+"分别为:"+str(self.main_class_instance.id)+" "+str(self.sub_class_instance.id))

    # 准备下列材料
    view = None
    like = None
    dislike = None
    reply = None
    user = None
    def get_data_ready(self,obj):
        self.reply = len(obj['comment'])
        self.like = random.choice(range(0,201))
        self.dislike = random.choice(range(0,21))
        self.view = random.choice(range(0,5000))+self.like
        self.user = ramdom_user()
        print('数据准备完毕:')
        print("view:",self.view,"like:",self.like,"dislike:",self.dislike,"reply:",self.reply,"user:"+self.user.username)
        pass


    def handle(self, *args, **options):
        self.before_handle()
        f_name = self.filename
        f = open('fake/fake_threads/'+f_name, encoding='utf-8')
        s = json.load(f)

        s.reverse()

        # for i in s:
        #     if not i['tittle']:
        #         print(i)

        if not len(s):
            return
        j = 1
        for i in s:
            # if j < 19:
            #     j = j+1
            #     continue
            try:
                self.get_data_ready(i)

                t = Thread()
                t.main_class = self.main_class_instance
                t.sub_class = self.sub_class_instance

                t.tittle = i['tittle']
                if not '?' in t.tittle:
                    t.tittle = t.tittle+"?"

                print(str(j),t.tittle)
                j = j+1
                t.create_user = self.user
                if i['content']:
                    t.content = str(i['content'][0])
                else:
                    t.content = ""

                t.like = self.like
                t.dislike = self.dislike
                t.reply = self.reply
                t.view = self.view
                t.save()

                import jieba.posseg as pseg
                from forum.models import TAG
                accept_type = ['n', 'ns', 'eng', 'nr', 'l', 'vn', 'nz', 's', 'j', 'nt', 'nrt']
                s = t.tittle
                words = pseg.cut(s)
                for word, flag in words:
                    if flag in accept_type:
                        tag = TAG()
                        tag.thread = t
                        tag.name = word[:30]
                        tag.save()

                self.add_comment(t.id,i['comment'])
            except:
                pass


    def add_comment(self,tid,comment):
        for i in comment:
            if not i:
                continue
            cm = Comment()
            cm.thread_id = tid
            cm.content = i
            cm.create_user = ramdom_user()
            cm.dislike = 0
            like = random.choice(range(0,12))
            if like > 6:
                cm.like = 0
            else:
                cm.like = like
            cm.save()
        pass

