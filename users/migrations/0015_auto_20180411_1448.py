# Generated by Django 2.0 on 2018-04-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180411_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
    ]
