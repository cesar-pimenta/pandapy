from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index_blog(requets):
    lista = [
        'data',
        'linux',
        'django',
    ]

    list_post = Post.objects.filter(status='AP')

    data = {
        'name': 'curso de django 3',
        'list': lista,
        'posts': list_post
    }
    return render(requets, 'index.html', data)

def post_detail(requets, id):
    post = Post.objects.get(id=id)
    return render(requets, 'post_detail.html', {
        'post': post,
        })