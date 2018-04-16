from django import template
from django.db.models.aggregates import Count
from django.contrib.contenttypes.models import ContentType

from ..models import Post, Category, Tag
from users.models import User
from likes.models import Likes, LikesDetail

register = template.Library()
from likes.decorator import check_login, check_request

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_recent_user_posts(user, num=5):
    return Post.objects.filter(author=user).order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0).order_by('-id')

@register.simple_tag
def get_post_of_category(cate):
    return Post.objects.filter(category=cate)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_interesting_users():
    return User.objects.all()

