# Generated by Django 3.0.1 on 2020-02-26 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200226_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', models.ImageField(blank=True, upload_to='post_images')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 2, 26, 5, 47, 20, 109143, tzinfo=utc), verbose_name='Created Date')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Published Date')),
            ],
        ),
        migrations.DeleteModel(
            name='blog_post',
        ),
    ]
