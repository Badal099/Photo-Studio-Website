# Generated by Django 3.0.3 on 2021-04-01 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudioApp', '0010_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='item5',
        ),
    ]
