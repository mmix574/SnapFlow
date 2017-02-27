from django import forms

from .models import AddModel

class AddForm(forms.ModelForm):
    class Meta:
        model = AddModel
        fields = ['a1','a2']

    def save(self):
        print("saving...")
        return super(AddForm, self).save()