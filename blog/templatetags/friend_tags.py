from django import template
from django.db.models.aggregates import Count
from django.contrib.contenttypes.models import ContentType
import math
from ..models import Post, Category, Tag
from users.models import User
from likes.models import Likes, LikesDetail

register = template.Library()
from likes.decorator import check_login, check_request

@register.simple_tag
def get_likes_num(id):
    obj_type = "post"
    obj_id = id
    c = ContentType.objects.get(model=obj_type)
    try:
        l = Likes.objects.get(content_type = c, object_id = obj_id)
    except Exception as e:
        #没有获取到对象，则新增一个Likes对象
        l = Likes(content_type = c, object_id = obj_id)
    likes_num = l.likes_num
    return likes_num

@check_login
@register.simple_tag
def is_like(id, user):
    obj_type = "post"
    obj_id = id
    c = ContentType.objects.get(model=obj_type)
    try:
        l = Likes.objects.get(content_type = c, object_id = obj_id)
    except Exception as e:
        #没有获取到对象，则新增一个Likes对象
        return False
        # l = Likes(content_type = c, object_id = obj_id)
    try:
        detail = LikesDetail.objects.get(likes = l, user = user)
    except Exception as e:
        return False
        # detail = LikesDetail(likes = l, user = user, is_like = False)
    return detail.is_like

@register.simple_tag
def is_friend(user, author):
    try:
        user_friend = User.objects.get(username=user, friends__exact=author)
    except Exception as e:
        return False
    return True

@register.simple_tag
def get_hot_users():
    pass


# class recommandTuple:
#     def __init__(self, userA, userB, similarity):
#         self.userA = userA
#         self.userB = userB
#         self.similarity = similarity
#
#     def __repr__(self):
#         return repr(( self.userA.username,  self.userB.username, self.similarity))

@register.simple_tag
def get_similarity_of_user(userA, userB):
    dot_product = 0
    hobbyA_Value = 0
    for hobby in userA.hobbies.all():
        try:
            userB.hobbies.get(name=hobby.name)
            dot_product=dot_product+1
        except Exception as e:
            pass
        hobbyA_Value=hobbyA_Value+1
    hobbyB_Value=userB.hobbies.count()
    abs_value_product=math.sqrt(hobbyA_Value*hobbyB_Value)
    if abs_value_product==0:
        return (userA, userB, 0)
    else:
        return (userA, userB, dot_product*1.0/abs_value_product)


@register.simple_tag
def get_recommand_users(user):
    users = User.objects.all()
    user_tuples = []
    for userB in users:
        if user != userB:
            if not is_friend(user, userB):
                temp = get_similarity_of_user(user, userB)
                user_tuples.append(temp)
    user_tuples = sorted(user_tuples, key=lambda x: x[2], reverse=True)
    print(user_tuples)
    recommand_users = []
    for user_tuple in user_tuples[:6]:
        recommand_users.append(user_tuple[1])
    return recommand_users

@register.simple_tag
def get_friends(user):
    friends = []
    users = User.objects.all()
    for man in users:
        if man != user and is_friend(user, man):
            friends.append(man)
    return friends
