# Generated by Django 2.0 on 2018-04-11 13:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20180411_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
