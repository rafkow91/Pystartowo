from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField

from core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.SET_DEFAULT, related_name='posts_authors', default='User deleted')
    editor = models.ForeignKey('auth.User', on_delete=models.SET_DEFAULT,
                               related_name='posts_editors', blank=True, null=True,  default='User deleted')
    edited_at = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = models.ManyToManyField('tags.Tag', related_name='posts', blank=True)
    # TODO: to change destination folder to slug-name folder
    image_file = ImageField(upload_to='images/posts/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posty'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.editor:
            self.edited_at = None
        return super().save(*args, **kwargs)
