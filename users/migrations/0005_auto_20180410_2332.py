# Generated by Django 2.0 on 2018-04-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180410_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='/static/blog/portrait/default.png', upload_to='portrait'),
        ),
    ]