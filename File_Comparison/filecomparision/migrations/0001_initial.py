# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File_Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('file_field', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
    ]