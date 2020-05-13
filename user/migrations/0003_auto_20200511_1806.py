# Generated by Django 3.0.6 on 2020-05-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200511_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='jon', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
