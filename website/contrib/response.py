from django.shortcuts import render_to_response

def MessageResponse(tittle='tittle',content='content'):
    return render_to_response('index/message.html',context={'message_tittle':tittle,'message_content':content})






