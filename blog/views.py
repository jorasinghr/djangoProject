from django.shortcuts import render
from .models import Post
# Create your views here.
'''
posts = [
    {
        'author': 'Jora',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'December 31, 2020'
    },
    {
        'author': 'Jora123',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'December 31, 2020'
    },
]
'''


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

