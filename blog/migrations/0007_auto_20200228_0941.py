# Generated by Django 3.0.1 on 2020-02-28 04:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200226_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 4, 11, 37, 861890, tzinfo=utc), verbose_name='Created Date'),
        ),
    ]