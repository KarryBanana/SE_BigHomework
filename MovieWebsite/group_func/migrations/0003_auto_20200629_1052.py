# Generated by Django 3.0.7 on 2020-06-29 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_func', '0002_auto_20200628_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppost',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
