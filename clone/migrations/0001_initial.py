# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 17:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('photo', models.ImageField(null=True, upload_to='image/')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['bio'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('description', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.TextField()),
                ('rating', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
