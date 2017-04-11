from django.shortcuts import render
from .models import Comment

from index.appviews import AppBaseTemplateView
from .forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from website.utils import messages


from .models import Comment
from .forms import CommentForm


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class IndexView(AppBaseTemplateView):
    template_name = 'timeline/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        list = Comment.objects.all().order_by('-created_time')
        context['list'] = list
        return context

    def get(self, request,context={}, *args, **kwargs):
        # messages.success(request,"你已经成功啦!")
        return super(IndexView, self).get(request,context={}, *args, **kwargs)

    def post(self,request,context={},*args,**kwargs):
        content = request.POST.get("say_content",None)
        if content:
            print(content)
        else:
            print("None")


    #     #    user = models.ForeignKey(User)
    # tittle = models.CharField(max_length=20)
    # content = models.CharField(max_length=120)
    # created_time = models.DateTimeField(auto_now=True)
    # last_operate = models.DateTimeField(auto_now_add=True)


        f = CommentForm(request.POST)
        m = f.save(commit=False)
        m.user = request.user

        if f.is_valid():
            f.save()
        else:
            print("not validate")


        return super(IndexView, self).post(request,context={},*args,**kwargs)

