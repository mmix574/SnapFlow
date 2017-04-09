from django import forms
from .models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         field = ['tittle','content']

        # user = models.ForeignKey(User)
        # tittle = models.CharField(max_length=20)
        # content = models.CharField(max_length=120)
        # created_time = models.DateTimeField(auto_now=True)
        # last_operate = models.DateTimeField(auto_now_add=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    pass