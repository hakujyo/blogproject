from django import template
from django.db.models.aggregates import Count
from django.contrib.contenttypes.models import ContentType
import math
from ..models import Post, Category, Tag
from users.models import User
from likes.models import Likes, LikesDetail

register = template.Library()

@register.simple_tag
def get_similarity_of_post(postA, postB):
    dot_product = 0
    tagA_Value = 0
    for tag in postA.tags.all():
        try:
            postB.tags.get(name=tag.name)
            dot_product=dot_product+1
        except Exception as e:
            pass
        tagA_Value=tagA_Value+1
    tagB_Value=postB.tags.count()
    abs_value_product=math.sqrt(tagA_Value*tagB_Value)
    if abs_value_product==0:
        return (postA, postB, 0)
    else:
        return (postA, postB, dot_product*1.0/abs_value_product)

@register.simple_tag
def get_recommand_posts(post):
    posts = Post.objects.all()
    post_tuples=[]
    for postB in posts:
        if post != postB:
            print(postB)
            temp = get_similarity_of_post(post, postB)
            post_tuples.append(temp)
    post_tuples = sorted(post_tuples, key=lambda x:x[2], reverse=True)
    recommand_posts=[]
    print(post_tuples)
    for user_tuple in post_tuples[:6]:
        recommand_posts.append(user_tuple[1])
    return recommand_posts