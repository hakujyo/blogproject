from django import template
from django.db.models.aggregates import Count
from django.contrib.contenttypes.models import ContentType

from ..models import Post, Category, Tag
from users.models import User
from likes.models import Likes, LikesDetail

register = template.Library()
from likes.decorator import check_login, check_request

@register.simple_tag
def is_friend(user, author):
    try:
        user_friend = User.objects.get(username=user, friends__exact=author)
    except Exception as e:
        return False
    return True
