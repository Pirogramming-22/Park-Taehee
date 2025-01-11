from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'year', 'genre', 'score', 'time', 'review', 'director', 'actor']
        labels = {
            'title': '제목',
            'year': '개봉년도',
            'genre': '장르',
            'score': '별점',
            'time': '러닝타임',
            'review': '리뷰',
            'director': '감독',
            'actor': '배우',
        }