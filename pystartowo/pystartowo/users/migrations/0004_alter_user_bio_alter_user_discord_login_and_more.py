# Generated by Django 4.1.1 on 2022-10-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_delete_userbio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, verbose_name="O mnie"),
        ),
        migrations.AlterField(
            model_name="user",
            name="discord_login",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Login z Diskord'a DoKodu.it"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Imię i nazwisko"
            ),
        ),
    ]