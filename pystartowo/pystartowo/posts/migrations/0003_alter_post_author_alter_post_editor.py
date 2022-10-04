# Generated by Django 4.1.1 on 2022-10-04 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0002_alter_post_image_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default="User deleted",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="posts_authors",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="editor",
            field=models.ForeignKey(
                blank=True,
                default="User deleted",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="posts_editors",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]