# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160514_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='zipCode',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]