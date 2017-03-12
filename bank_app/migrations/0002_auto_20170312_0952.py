# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievementresource',
            name='resource',
            field=models.FileField(blank=True, null=True, upload_to='resource/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(upload_to='avatar/%Y/%m/%d/'),
        ),
        migrations.AlterModelTable(
            name='achievementresource',
            table='achievement_resource',
        ),
        migrations.AlterModelTable(
            name='achievements',
            table='achievements',
        ),
        migrations.AlterModelTable(
            name='cards',
            table='cards',
        ),
        migrations.AlterModelTable(
            name='labels',
            table='labels',
        ),
        migrations.AlterModelTable(
            name='observers',
            table='observers',
        ),
        migrations.AlterModelTable(
            name='userlabels',
            table='user_labels',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]