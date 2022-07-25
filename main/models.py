from django.db import models
from django.utils.timezone import timedelta, now
from django.utils.text import slugify

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    bio = models.TextField()


class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        i = 0
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        i += 1
                        slug += f'-{i}'
                    else:
                        break

            self.slug = slug

        return super().save(*args, **kwargs)
