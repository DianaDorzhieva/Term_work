# Generated by Django 4.2.6 on 2024-01-31 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_fio_user_author_user_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='author',
        ),
    ]
