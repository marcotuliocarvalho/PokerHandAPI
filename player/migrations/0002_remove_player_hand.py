# Generated by Django 3.2.4 on 2021-06-24 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='hand',
        ),
    ]