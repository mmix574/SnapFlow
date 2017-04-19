from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from index.appviews import AppBaseTemplateView
from index.contrib.response import MessageResponse
from .models import Class
from .models import SubClass
from .models import Thread

# 定义默认tab
def get_default_tab():
    return "technique"

class IndexView(AppBaseTemplateView):
    template_name = 'forum/index.html'

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        return super().post(request, context, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        display_class = Class.objects.all().order_by('order')
        if not (len(context)):
            return MessageResponse("提示","没有任何的ThreadType，请在数据库中先添加")
        context['display_class'] = display_class

        tab = get_default_tab()
        subtab = None

        # tab 控制
        if self.request.GET.get('tab',None) and self.request.GET.get('subtab',None):
            tab = self.request.GET.get('tab',None)
            subtab = self.request.GET.get('subtab',None)
        elif self.request.GET.get('tab',None):
            tab = self.request.GET.get('tab',None)
        elif self.request.COOKIES.get('tab',None) and self.request.COOKIES.get('subtab',None):
            tab = self.request.COOKIES.get('tab',None)
            subtab = self.request.COOKIES.get('subtab',None)

        if subtab=="None":
            subtab = None


        context['tab'] = tab
        tab_instance = Class.objects.filter(name=tab)
        if not tab_instance:
            return context

        display_sub_class = SubClass.objects.filter(parent_class=tab_instance[0])
        if not display_sub_class:
            return context
        context['display_sub_class'] = list(display_sub_class)

        context['subtab'] = subtab
        content_list = {}
        # 2017年4月15日20:03:14
        p = int(self.request.GET.get('p',1))
        if p<=0:
            p=1

        per_page = 20
        count = 0
        if tab and subtab:
            subtab_instance = SubClass.objects.get(name=subtab)
            count = Thread.objects.filter(main_class=tab_instance,sub_class=subtab_instance).count()
            content_list = Thread.objects.filter(main_class=tab_instance,sub_class=subtab_instance).order_by('-create_time')[((p-1)*20):(p)*20]
        elif tab:
            content_list = Thread.objects.filter(main_class=tab_instance).order_by('-create_time')[((p-1)*20):(p)*20]
            count=Thread.objects.filter(main_class=tab_instance).count()


        import math
        page_count = math.ceil(count/per_page)

        context['p'] = p
        context['page_count'] = page_count
        context['content_list'] = content_list


        self.set_cooke('tab',tab)
        self.set_cooke('subtab',subtab)


        return context


import json

from .forms import ThreadForm
from django.http.response import HttpResponseRedirect
@method_decorator(login_required,name='dispatch')
class CreateView(AppBaseTemplateView):
    template_name = 'forum/create.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        sub_class =SubClass.objects.all()
        res = []
        for i in sub_class:
            res.append({"parent_class_name":i.parent_class.display_name,"parent_class_id":i.parent_class.id,"sub_class_id":i.id,"name":i.name,"display_name":i.display_name})

        context['clsss_list'] = json.dumps(res)

        context['form'] = ThreadForm()
        return context

    def get(self, request, context={}, *args, **kwargs):
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        d = request.POST
        d.update({'create_user':request.user.id})
        tf = ThreadForm(d)

        if tf.is_valid():
            m = tf.save()
            return HttpResponseRedirect("/t/"+str(m.id))
        else:
            print(tf.errors)

        # return HttpResponseRedirect("/t/"+str(tf.auto_id))
        return super().post(request, context, *args, **kwargs)


class SearchView(AppBaseTemplateView):
    template_name = 'forum/search.html'

    def get(self, request, context={}, *args, **kwargs):
        query = request.GET.get('q',None)
        if not query:
            return super().get(request, {"query":query}, *args, **kwargs)

        search_list = Thread.objects.filter(tittle__contains=query)

        # print(search_list)
        return super().get(request, {"query":query,"search_list":search_list}, *args, **kwargs)


from django.core.urlresolvers import reverse
from index.views import MessageView

from index.contrib.response import _Http404
from forum.forms import CommentForm
from .models import Comment

from .models import ThreadLike
from collection.models import Collection

class DetailView(AppBaseTemplateView):
    template_name = 'forum/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, context={}, *args, **kwargs):
        if not 'id' in self.kwargs:
            return HttpResponseRedirect(reverse('_finding'))

        id = self.kwargs['id']
        try:
            t = Thread.objects.get(id=id)
            t.view = t.view+1
            t.save()
        except Exception as e:
            pass


        try:
            thread = Thread.objects.get(id=id)
        except Exception as e:
            return _Http404(request)

        comment_form = CommentForm()

        # get comment list from databases
        comment_list = Comment.objects.filter(thread_id=id)



        # get like from databased
        liked = False
        if request.user.is_authenticated():
            tl = ThreadLike.objects.filter(thread=thread,user=request.user)
            if tl:
                liked = True

        # get_collected from database
        collected = False
        if request.user.is_authenticated():
            cl = Collection.objects.filter(thread=thread,create_user=request.user)
            if cl:
                collected = True



        return super().get(request, {'thread':thread,'tid':id,'comment_form':comment_form,"comment_list":comment_list,"liked":liked,"collected":collected}, *args, **kwargs)


    def post(self, request, context={}, *args, **kwargs):
        if not 'id' in self.kwargs:
            return HttpResponseRedirect(reverse('_finding'))

        id = self.kwargs['id']

        try:
            thread = Thread.objects.get(id=id)
        except Exception as e:
            return _Http404(request)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            m = comment_form.save(commit=False)
            m.create_user = request.user
            m.thread_id = id
            m.save()
            try:
                t = Thread.objects.get(id=id)
                t.reply = t.reply+1
                t.save()
            except Exception as e:
                pass

        # get comment list from databases
        comment_list = Comment.objects.filter(thread_id=id)
        # get comment list from databases
        return super().post(request, {'thread':thread,'tid':id,'comment_form':comment_form,"comment_list":comment_list}, *args, **kwargs)



from index.contrib.response import MessageResponse
from django.http.response import HttpResponseRedirect
@method_decorator(login_required,name="dispatch")
class FindingActionView(AppBaseTemplateView):
    template_name = 'forum/action.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tid = self.kwargs['id']
        action = self.kwargs['action']
        thread = Thread.objects.filter(id=tid)
        if thread:
            thread = thread[0]
        else:
            thread = {}

        context['action'] = action
        context['thread'] = thread
        return context

    def get(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse('你没有权限访问这个页面',"")
        return super().get(request, context, *args, **kwargs)

    def post(self, request, context={}, *args, **kwargs):
        if not self.validate():
            return MessageResponse('你没有权限访问这个页面',"")


        tid = request.POST.get('tid',None)
        action = request.POST.get('action',None)

        if action=="delete":
            try:
                thread = Thread.objects.get(id=tid)
                thread.delete()
            except Exception as e:
                pass
            finally:
                return HttpResponseRedirect("/t")


        return super().post(request, context, *args, **kwargs)

    def validate(self):
        user = self.request.user
        if not user.is_authenticated():
            return False
        elif not user.is_staff:
            return False
        return True



