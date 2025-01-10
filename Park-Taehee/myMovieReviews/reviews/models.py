from django.db import models
from django.conf import settings
# Create your models here.
class Reviews(models.Model):
    genre_choices=[
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('SF', 'SF'),
        ('Sports', 'Sports'),
        ('Fantasy', 'Fantasy'),
    ]
    title=models.CharField(max_length=20)
    year=models.CharField(max_length=5)
    genre=models.CharField(max_length=10, choices=genre_choices)
    score=models.CharField(max_length=4)
    time=models.IntegerField()
    review=models.TextField()
    director=models.CharField(max_length=20)
    actor=models.CharField(max_length=20)

    def __str__(self):
        return self.title