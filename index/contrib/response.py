from django.shortcuts import render_to_response


# 这里有bug，没有加载用户信息直接输出了消息.
def MessageResponse(tittle='tittle',content='content'):
    return render_to_response('index/message.html', context={'message_tittle':tittle, 'message_content':content})






