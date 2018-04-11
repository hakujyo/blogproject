# Generated by Django 2.0 on 2018-04-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]