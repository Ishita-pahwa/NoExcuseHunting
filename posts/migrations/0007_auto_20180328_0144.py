# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-28 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180328_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='photos', to='posts.Tag'),
        ),
    ]
