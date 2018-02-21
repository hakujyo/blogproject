from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})

def home(request):
    return render(request, 'home.html')

def teststring(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'teststring.html', {'string': string})