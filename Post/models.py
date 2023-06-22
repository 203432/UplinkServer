from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    text = models.CharField(max_length=100)
    published = models.DateField(auto_now_add=True)
    media = models.FileField(null=True,blank=True,default='',upload_to='media/')
    image = models.ImageField(null=True,blank=True,default='',upload_to='images/')
    num_likes = models.IntegerField(default=0)
