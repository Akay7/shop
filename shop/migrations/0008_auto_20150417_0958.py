# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_positioninorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='detail',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='positioninorder',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
