# Generated by Django 2.0 on 2018-04-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20180411_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.IntegerField(blank=True, choices=[(1, '高中或以下学历'), (2, '学士'), (3, '硕士'), (4, '博士'), (5, '博士后')], null=True, verbose_name='学历'),
        ),
    ]