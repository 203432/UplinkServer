from django.db import models
from django.contrib.auth.models import User

from Post.models import Post

# Create your models here.

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    text = models.CharField(max_length=200)
    
