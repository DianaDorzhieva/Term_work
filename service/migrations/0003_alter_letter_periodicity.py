# Generated by Django 5.0 on 2024-01-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_letter_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='periodicity',
            field=models.IntegerField(choices=[('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц')], verbose_name='переодичность рассылки'),
        ),
    ]
