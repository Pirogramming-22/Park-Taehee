from django.contrib.auth.models import User
from django.db import models
from PIL import Image, ImageOps

class Posts(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='idea_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        
        if self.image:  
            img_path = self.image.path
            img = Image.open(img_path)

            max_size = (200, 200)  
            img = ImageOps.exif_transpose(img)  
            img.thumbnail(max_size, Image.Resampling.LANCZOS)  

            img.save(img_path, quality=85)

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

    def __str__(self):
        return self.text[:20]