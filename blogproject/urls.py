from django.conf.urls import url, include
from django.contrib import admin
from blog.feeds import AllPostsRssFeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^likes/', include('likes.urls')),
    url(r'^all/rss/(?P<pk>[0-9]+)/$', AllPostsRssFeed(), name='rss'),
]
