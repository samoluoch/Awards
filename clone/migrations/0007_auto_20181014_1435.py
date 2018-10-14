# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-14 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0006_auto_20181014_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentrating',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Profile'),
        ),
        migrations.AlterField(
            model_name='designrating',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Profile'),
        ),
        migrations.AlterField(
            model_name='usabilityrating',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Profile'),
        ),
    ]