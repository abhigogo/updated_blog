# Generated by Django 3.0.1 on 2020-02-26 05:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200226_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 5, 27, 14, 874876, tzinfo=utc), verbose_name='Created Date'),
        ),
    ]