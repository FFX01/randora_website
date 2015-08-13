# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150810_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default='justin', max_length=120),
            preserve_default=False,
        ),
    ]
