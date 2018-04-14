from django import template
from django.db.models.aggregates import Count
from django.contrib.contenttypes.models import ContentType

from ..models import Post, Category, Tag
from users.models import User
from likes.models import Likes, LikesDetail

register = template.Library()
from likes.decorator import check_login, check_request


CHOICE_GENDER = {1: '男', 2: '女'}
CHOICE_EDU = {1: '高中或以下学历', 2: '学士', 3: '硕士', 4: '博士', 5: '博士后'}

@register.simple_tag
def get_users():
    return User.objects.all()

@register.simple_tag
def get_recent_users(num=5):
    return User.objects.all().order_by('-id')[:num]

@register.simple_tag
def get_gender(author):
    return CHOICE_GENDER[author.sex]

@register.simple_tag
def get_edu(author):
    return CHOICE_EDU[author.education]