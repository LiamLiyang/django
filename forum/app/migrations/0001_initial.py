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
            name='Access_Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user_ip', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=30)),
                ('access_time', models.DateTimeField(help_text='訪問時間')),
                ('end_time', models.DateTimeField(help_text='結束時間')),
                ('sitckid', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_acess_record',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_classifcation',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('comment_body', models.TextField()),
            ],
            options={
                'db_table': 'tb_comment',
            },
        ),
        migrations.CreateModel(
            name='Sitck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('additional_content', models.TextField()),
                ('like', models.PositiveIntegerField(default=0)),
                ('access', models.PositiveIntegerField(default=0)),
                ('rectime', models.DateTimeField(auto_now=True)),
                ('last_access', models.DateTimeField(auto_now_add=True)),
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
