from django.shortcuts import render_to_response


# 这里有bug，没有加载用户信息直接输出了消息.
def MessageResponse(tittle='tittle',content='content'):
    return render_to_response('index/message.html', context={'message_tittle':tittle, 'message_content':content})



from index.views import MessageView
def _Http404(request):
    return MessageView.as_view(tittle="404", message="抱歉没有找到网页",status=404)(request)




