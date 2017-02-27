from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
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

    else:
        form = AddForm()

    return render(request,"lab/form.html",{"form":form})