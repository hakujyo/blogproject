import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})


def home(request):
    return render(request, 'home.html')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})