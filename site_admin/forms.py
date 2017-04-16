from django.forms.models import ModelForm
from .models import AdminBroadCast

class AdminBroadCastForm(ModelForm):
    class Meta:
        model = AdminBroadCast
        fields = ['tittle','content']