from django import forms

from .models import AddModel

from django.core.exceptions import ObjectDoesNotExist

class AddForm(forms.ModelForm):
    class Meta:
        model = AddModel
        fields = ['a1','a2']

    # def save(self,*args,**kwargs):
    #     print("saving...")
    #     return super(AddForm, self).save(args,kwargs)

    def save(self, commit=True):
        return super().save(commit)



from .models import PostModel

class PostForm(forms.ModelForm):

    #
    # def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
    #              label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None):
    #     super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
    #                      use_required_attribute)


    class Meta:
        model = PostModel
        fields = ['tittle','content']