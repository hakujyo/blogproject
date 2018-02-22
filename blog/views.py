import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})

def home(request):
    return render(request, 'home.html')

def teststring(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'teststring.html', {'string': string})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})