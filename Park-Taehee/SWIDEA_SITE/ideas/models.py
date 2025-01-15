from django.db import models
from PIL import Image, ImageOps
from django.contrib.auth.models import User
# Create your models here.
class Ideas(models.Model):
    SORT_CHOICES = [
        ('interest', '찜하기순'),
        ('name', '이름순'),
        ('created_at', '등록순'),
        ('latest', '최신순'),
    ]
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='idea_images/')
    content=models.TextField()
    interest=models.IntegerField(default=0)
    devtool=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    interest = models.IntegerField(default=0)
    genre_choices = models.CharField(max_length=10, choices=SORT_CHOICES, default='created_at')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        
        if self.image:  
            img_path = self.image.path
            img = Image.open(img_path)

            max_size = (200, 200)  
            img = ImageOps.exif_transpose(img)  
            img.thumbnail(max_size, Image.Resampling.LANCZOS)  

            img.save(img_path, quality=85)

class IdeaStar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    idea=models.ForeignKey(Ideas, on_delete=models.CASCADE, related_name='stars')

    class Meta:
        unique_together=('user','idea')

    def __str__(self):
        return f"{self.user.username}-{self.idea.title}"