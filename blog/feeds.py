from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Post
from users.models import User


class AllPostsRssFeed(Feed, ListView):
    def get_object(self, request, pk):
        return User.objects.get(pk=pk)

    # 显示在聚合阅读器上的标题
    def title(self, obj):
        return "%s的部落格" % obj.username

    # 显示在聚合阅读器上的描述信息
    def description(self, obj):
        return "%s的部落格" % obj.username

    # 通过聚合阅读器跳转到网站的地址
    def link(self, obj):
        return obj.get_absolute_url()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 需要显示的内容条目
    def items(self, obj):
        auth = get_object_or_404(User, pk=obj.pk)
        post_list = Post.objects.filter(author=auth)
        return post_list

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body