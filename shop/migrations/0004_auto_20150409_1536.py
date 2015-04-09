# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150407_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
