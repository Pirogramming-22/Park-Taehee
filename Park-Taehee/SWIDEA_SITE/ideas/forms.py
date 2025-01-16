from django import forms
from .models import Ideas

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ['title', 'image', 'content', 'interest', 'devtool']
        labels = {
            'title': '아이디어명',
            'image': 'Image',
            'content': '아이디어 설명',
            'interest': '아이디어 관심도',
            'devtool': '예상 개발툴',
        }