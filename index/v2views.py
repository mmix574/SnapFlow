from django.shortcuts import render
from django.views.generic import TemplateView

class V2Index(TemplateView):
    template_name = 'v2index/w.html'

    def get_context_data(self, **kwargs):
        return super(V2Index, self).get_context_data(**kwargs)


    def get(self, request, *args, **kwargs):
        return super(V2Index, self).get( request, *args, **kwargs)



class RegisterView(TemplateView):
    template_name = "v2index/w.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);
        context['view'] = "register"
        return context


class LoginView(TemplateView):
    template_name = "v2index/w.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);
        context['view'] = "login"
        return context

