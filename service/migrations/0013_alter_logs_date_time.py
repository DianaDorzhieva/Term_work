# Generated by Django 4.2.9 on 2024-02-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_remove_message_letter_letter_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки'),
        ),
    ]