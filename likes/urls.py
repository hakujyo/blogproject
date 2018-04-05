from django.conf.urls import url
from . import views

app_name = 'likes'
urlpatterns = [
    url(r'^likes_change$', views.likes_change, name='likes_change'),
    url(r'^likes_nums$',views.likes_nums, name='likes_nums'),
]
