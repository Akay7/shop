# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20150417_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninorder',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
