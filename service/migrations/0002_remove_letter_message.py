# Generated by Django 4.2.9 on 2024-02-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='message',
        ),
    ]