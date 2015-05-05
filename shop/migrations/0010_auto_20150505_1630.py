# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20150418_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninorder',
            name='product',
            field=models.ForeignKey(to='shop.Product'),
        ),
    ]
