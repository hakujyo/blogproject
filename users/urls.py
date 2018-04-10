from django.conf.urls import url

from . import views


app_name = 'users'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^welcome/$', views.index, name='index'),
    url(r'^image/upload/$', views.UploadImageView.as_view(), name="image_upload"),
]