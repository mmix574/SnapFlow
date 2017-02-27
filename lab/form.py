from django import forms

from .models import AddModel

class Addform(forms.ModelForm):
    class Meta:
        model = AddModel
        fields = ('a1','a2')