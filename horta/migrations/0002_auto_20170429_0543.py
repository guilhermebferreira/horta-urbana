# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
