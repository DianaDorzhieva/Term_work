# Generated by Django 4.2.9 on 2024-02-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_remove_logs_last_mailing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date_time',
            field=models.DateTimeField(verbose_name='дата и время последней попытки'),
        ),
    ]