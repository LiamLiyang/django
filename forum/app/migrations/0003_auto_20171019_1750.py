# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171019_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitck',
            name='additional_content',
            field=models.TextField(default=None, blank=True),
        ),
    ]
