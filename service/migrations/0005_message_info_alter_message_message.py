# Generated by Django 4.2.9 on 2024-02-03 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_message_user_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.letter', verbose_name='настройка сообщения'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='тело письма'),
        ),
    ]