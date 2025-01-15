from django import forms
from .models import DevTools

class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTools
        fields = ['name', 'kind', 'content']
        labels = {
            'name': '이름',
            'kind': '종류',
            'content': '개발툴 설명',
        }