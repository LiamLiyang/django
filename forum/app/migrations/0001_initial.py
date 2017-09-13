# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_classifcation',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('comment_body', models.TextField()),
            ],
            options={
                'db_table': 'tb_comment',
            },
        ),
        migrations.CreateModel(
            name='Sitck',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('additional_content', models.TextField()),
                ('like', models.PositiveIntegerField()),
                ('access', models.PositiveIntegerField()),
                ('rectime', models.DateTimeField()),
                ('last_access', models.DateTimeField()),
                ('cfn', models.ForeignKey(to='app.Classification')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_sitck',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='sitck',
            field=models.ForeignKey(to='app.Sitck'),
        ),
    ]
