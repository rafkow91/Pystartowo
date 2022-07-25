from distutils.command.upload import upload
from django.db import models

from main.models import SlugMixin, Timestamped


class PostModel(Timestamped, SlugMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=False)
    images = models.ImageField(upload_to=f'posts/{slug}')
    tags = models.ManyToManyField('tags.Tag', related_name='posts', blank=True)