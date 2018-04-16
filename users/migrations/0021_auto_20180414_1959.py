# Generated by Django 2.0 on 2018-04-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180228_1651'),
        ('users', '0020_auto_20180411_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hobbies',
        ),
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]