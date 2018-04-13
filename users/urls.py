from django.conf.urls import url

from . import views


app_name = 'users'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^welcome/$', views.index, name='index'),
    url(r'^add_friend/(?P<pk>[0-9]+)/$', views.add_friend, name='add_friend'),
    url(r'^delete_friend/(?P<pk>[0-9]+)/$', views.delete_friend, name='delete_friend'),
    url(r'^image/upload/$', views.UploadImageView.as_view(), name="image_upload"),
]