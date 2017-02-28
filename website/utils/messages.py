from django.contrib import messages


def info(request,message):
    messages.info(request,message,extra_tags="info")

def success(request,message):
    messages.success(request,message,extra_tags="success")

def warning(request,message):
    messages.warning(request,message,extra_tags="warning")

def danger(request,message):
    messages.error(request,message,extra_tags="danger")