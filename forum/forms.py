from django import forms
from .models import Thread
from .models import Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ["create_user",'sub_class','tittle','content']



# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment