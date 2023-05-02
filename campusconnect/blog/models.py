# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
class SearchLog(models.Model):
    url = models.CharField(max_length=255)
    iswp = models.BooleanField(default=False)
    search_time = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title