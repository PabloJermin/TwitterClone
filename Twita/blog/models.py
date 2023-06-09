from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(max_length = 100, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title