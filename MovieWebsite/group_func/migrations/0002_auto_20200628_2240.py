# Generated by Django 3.0.7 on 2020-06-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_func', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
