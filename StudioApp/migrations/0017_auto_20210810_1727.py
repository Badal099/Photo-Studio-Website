# Generated by Django 3.0.3 on 2021-08-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudioApp', '0016_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sports', models.ImageField(default='', upload_to='sports')),
            ],
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
