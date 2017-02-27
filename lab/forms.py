from django import forms

from .models import AddModel

class AddForm(forms.ModelForm):
    class Meta:
        model = AddModel
        fields = ['a1','a2']

    # def save(self,*args,**kwargs):
    #     print("saving...")
    #     return super(AddForm, self).save(args,kwargs)

    def save(self, commit=True):
        return super().save(commit)

