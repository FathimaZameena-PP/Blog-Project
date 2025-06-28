from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=75)
    body=models.TextField()
    slug=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='', default='1.png', blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

    
        