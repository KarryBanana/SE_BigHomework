# Generated by Django 3.0.5 on 2020-06-13 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_moviecomment_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecomment',
            name='state',
        ),
    ]