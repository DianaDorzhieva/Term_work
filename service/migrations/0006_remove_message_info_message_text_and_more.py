# Generated by Django 4.2.9 on 2024-02-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_message_info_alter_message_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='info',
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='тело письма'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.letter', verbose_name='настройка сообщения'),
        ),
    ]
