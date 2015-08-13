# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 10, 21, 28, 51, 274718, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
