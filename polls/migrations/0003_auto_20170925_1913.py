# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_test_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test_field',
            new_name='choices',
        ),
    ]
