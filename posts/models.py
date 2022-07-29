from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.utils.text import slugify

from main.models import SlugMixin, Timestamped


class Post(Timestamped, SlugMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(blank=False)
    images = models.ImageField(upload_to=f'posts/{slug}')
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    modified_by = models.ManyToManyField('auth.User', related_name='editors', blank=True)
    tags = models.ManyToManyField('tags.Tag', related_name='posts', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)