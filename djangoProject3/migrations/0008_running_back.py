# Generated by Django 3.2.9 on 2021-12-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject3', '0007_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Running_Back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Back', models.CharField(max_length=255)),
            ],
        ),
    ]
