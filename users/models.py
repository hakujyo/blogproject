from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import blog

CHOICE_GENDER = ((1, '男'), (2, '女'))
CHOICE_EDU = ((1, '高中或以下学历'), (2, '学士'), (3, '硕士'), (4, '博士'), (5, '博士后'))

@python_2_unicode_compatible
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    image = models.ImageField('头像', upload_to="portrait", default=u"/static/blog/portrait/default.png", max_length=100)
    friends = models.ManyToManyField('self', symmetrical=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    birth = models.DateField('生日', blank=True, null=True)
    sex = models.IntegerField('性别', choices=CHOICE_GENDER, blank=True, null=True)
    hobbies = models.CharField('爱好', max_length=100, blank=True, null=True)
    education = models.IntegerField('学历',choices=CHOICE_EDU, blank=True, null=True)
    school = models.CharField('学校', max_length=20, blank=True, null=True)
    introduction = models.CharField('个人简介', max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:author', kwargs={'pk': self.pk})

    class Meta(AbstractUser.Meta):
        pass

