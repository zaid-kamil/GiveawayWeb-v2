# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20170511_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='giveaway_id',
        ),
    ]
