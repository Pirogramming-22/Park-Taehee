from django import forms
from .models import Posts, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'image',]
        labels = {
            'content': '추가하고 싶은 문구',
            'image': 'Image',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '댓글 입력',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'placeholder': '댓글을 입력하세요...'}),
        }