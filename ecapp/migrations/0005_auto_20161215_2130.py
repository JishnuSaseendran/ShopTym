# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-15 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0004_item_item_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='album_logo',
        ),
        migrations.AddField(
            model_name='item',
            name='item_logo',
            field=models.FileField(default=1000, upload_to=''),
            preserve_default=False,
        ),
    ]