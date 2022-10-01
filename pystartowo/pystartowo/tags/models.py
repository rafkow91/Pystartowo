from django.db import models
from django.utils.text import slugify

from core.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
