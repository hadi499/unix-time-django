from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    post = Post.objects.get(id=9)
    a = post.created_at
    print(type(a))
    print(a)

    return render(request, 'index.html', {'posts': posts})
