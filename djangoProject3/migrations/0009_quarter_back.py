# Generated by Django 3.2.9 on 2021-12-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject3', '0008_running_back'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quarter_Back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QB', models.CharField(max_length=255)),
            ],
        ),
    ]