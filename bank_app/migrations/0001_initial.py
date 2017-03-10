# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_data', models.DateTimeField(auto_created=True)),
                ('resource_type', models.IntegerField()),
                ('resource_id', models.IntegerField()),
                ('resource', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_data', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Observers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Cards')),
            ],
        ),
        migrations.CreateModel(
            name='UserLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Achievements')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Labels')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('about_user', models.TextField()),
                ('mail_address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('avatar', models.ImageField(upload_to='')),
                ('level_points', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='userlabels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Users'),
        ),
        migrations.AddField(
            model_name='observers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Users'),
        ),
        migrations.AddField(
            model_name='cards',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Users'),
        ),
        migrations.AddField(
            model_name='achievements',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Cards'),
        ),
        migrations.AddField(
            model_name='achievementresource',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.Achievements'),
        ),
    ]