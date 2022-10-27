from tokenize import group
from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField

from core.models import BaseModel
from core.utils import MailSender
from users.models import User


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text='Rozwiń to co opisałeś w tytule')
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        related_name='posts_authors',
        null=True,
    )
    editor = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        related_name='posts_editors',
        blank=True,
        null=True,
    )
    edited_at = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = models.ManyToManyField(
        'tags.Tag',
        related_name='posts',
        blank=True,
        help_text='Moduły, których dotyczy zagadnienie'
    )

    # TODO: to change destination folder to slug-name folder
    image_file = ImageField(
        upload_to='images/posts/%Y/%m/%d',
        blank=True,
        null=True,
        help_text='Tu możesz załączyć przykładowy kod, najlepiej w formie obrazka wykonanego przy użyciu np. CodeSnap czy Screenify'
    )

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
        
        user = User.objects.get(username=self.author)
        groups = user.groups.all()
        posts = Post.objects.filter(author=user).filter(published=True).count()
        

        return super().save(*args, **kwargs)


class ToAdd(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(
        help_text='Rozwiń to co opisałeś w tytule'
    )
    tags = models.ManyToManyField(
        'tags.Tag',
        related_name='to_add',
        blank=True,
        help_text='Pozwoli nam to odpowiedzieć na pytanie w sposób zrozumiały dla Ciebie i odpowiedni do Twojego poziomu wiedzy',
    )
    email = models.EmailField(
        blank=True,
        null=True,
        help_text='Podaj swojego maila a poinformujemy Cię kiedy odpowiedź na Twoje pytanie będzie gotowa',
    )
    realised = models.BooleanField(default=False)
    realised_by = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        related_name='to_add_realisator',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Do uzupełnienia'
        verbose_name_plural = 'Do uzupełnienia'

    def _send_mail(self, *agrs, **kwargs):
        mailbox = MailSender()
        title = str(self.title)
        print(mailbox, title)
        mailbox.send_mail(title)

    def save(self, *args, **kwargs):
        self._send_mail()
        return super().save(*args, **kwargs)
