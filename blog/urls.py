from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^teststring/$', views.teststring, name='teststring'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]