from django.shortcuts import render
from .models import Comment

from index.appviews import AppBaseTemplateView
from .forms import CommentForm
class IndexView(AppBaseTemplateView):
    template_name = 'timeline/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        list = Comment.objects.all().order_by('-created_time')
        context['list'] = list
        return context



class CreateView(AppBaseTemplateView):
    template_name = "timeline/create.html"


    def get(self, request,context={}, *args, **kwargs):

        form = CommentForm()

        return super(CreateView, self).get(request,context={"form":form}, *args, **kwargs)

    def post(self,request,context={},*args,**kwargs):
        form = CommentForm(request.POST)

        model = form.save(commit=False)

        model.user = request.user

        model.save()

        return super(CreateView, self).post(request,context={},*args,**kwargs)



class DeleteView(AppBaseTemplateView):
    pass


class EditView(AppBaseTemplateView):
    pass


class DetailView(AppBaseTemplateView):
    pass


