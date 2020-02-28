# Generated by Django 3.0.1 on 2020-02-28 06:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200228_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 6, 37, 4, 736275, tzinfo=utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Text')),
                ('posted_date', models.DateTimeField(default=datetime.datetime(2020, 2, 28, 6, 37, 4, 736275, tzinfo=utc), verbose_name='Date Posted')),
                ('approved_comment', models.BooleanField(default=False, verbose_name='Approved')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]
