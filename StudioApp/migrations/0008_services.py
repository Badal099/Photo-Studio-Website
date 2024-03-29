# Generated by Django 3.0.3 on 2021-03-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudioApp', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('msg', models.TextField()),
                ('address', models.CharField(max_length=2000)),
                ('image', models.ImageField(default='', upload_to='urgent')),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]
