# Generated by Django 3.2.9 on 2021-12-02 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject3', '0003_yards'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Yards',
            new_name='Stat',
        ),
        migrations.RenameModel(
            old_name='Stats',
            new_name='Yard',
        ),
        migrations.RenameField(
            model_name='stat',
            old_name='Receiver',
            new_name='RunningBack',
        ),
        migrations.RenameField(
            model_name='yard',
            old_name='RunningBack',
            new_name='Receiver',
        ),
    ]
