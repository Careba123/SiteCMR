from django import forms
from .models import CMR

class CMRForm(forms.ModelForm):
    class Meta:
        model = CMR
        fields = ['file']
