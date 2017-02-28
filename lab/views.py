from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.views.generic.base  import TemplateView
from django.http.response import HttpResponse

class IndexView(View):
    template_name = 'lab/index.html'

    def get(self, request, *args, **kwargs):
        # return super(IndexView, self).get(request,*args,**kwargs)
        return render(request, self.template_name)



    def post(self,request):
        # return super(IndexView, self).post(request);
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)
        # return

from .forms import AddForm

def create(request):
    if request.method=="POST":
        form = AddForm(request.POST)
        model = form.save(commit=False)
        model.result = model.a1+model.a2
        model.save()
        print(request.POST)
    else:
        form = AddForm()
        print(form)
    return render(request,"lab/form.html",{"form":form})



from .forms import PostForm

class PostView(TemplateView):
    template_name = 'lab/post.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import PostModel

@method_decorator(login_required, name='dispatch')
class PostEditView(TemplateView):
    template_name = 'lab/post.html'

    def get(self, request, *args, **kwargs):

        models = PostModel.objects.filter(user=request.user).order_by("time").reverse()

        for m in models:
            print(m)

        form = PostForm(instance=models[0])

        return render(request,self.template_name,{"form":form})


    def post(self,request,*args,**kwargs):
        form = PostForm(request.POST)
        f = form.save(commit=False)
        f.user = request.user
        f.save()
        return render(request,self.template_name,{"form":form})



