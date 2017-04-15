from django.shortcuts import render

# Create your views here.
from index.appviews import AppBaseTemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required,name='dispatch')
class HistoryView(AppBaseTemplateView):
    template_name = 'history/history.html'
    pass

