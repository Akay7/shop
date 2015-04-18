# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150417_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=200)),
                ('comment_from_client', models.TextField(default='')),
                ('comment_from_admin', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PositionInOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('order', models.ForeignKey(to='shop.Order')),
                ('product', models.OneToOneField(to='shop.Product')),
            ],
        ),
    ]
