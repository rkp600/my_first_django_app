# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_deleted_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='state',
            new_name='sate',
        ),
    ]
