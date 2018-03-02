from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import blog

@python_2_unicode_compatible
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('blog:author', kwargs={'pk': self.pk})

    class Meta(AbstractUser.Meta):
        pass