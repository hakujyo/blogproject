from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.conf import settings

@python_2_unicode_compatible
class Comment(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE,)

    def __str__(self):
        return self.text[:20]