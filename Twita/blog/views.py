from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post


def home(request):
    user = User.objects.get(id=1)
    
    # post = Post.objects.all().first()
    post = user.post_set.all().first
    
    return render(request, 'blog/home.html', {"post": post})


def about (request):

    return render(request, 'blog/about.html')