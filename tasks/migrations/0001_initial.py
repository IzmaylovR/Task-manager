# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField(verbose_name=b'date published')),
                ('text', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
