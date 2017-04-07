from django.shortcuts import render
from .models import Comment

from index.appviews import AppBaseTemplateView
from .forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from website.utils import messages


from .models import Comment
from .forms import CommentForm

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


        f = CommentForm()

        if f.is_valid():
            f.save()


        return super(IndexView, self).post(request,context={},*args,**kwargs)

