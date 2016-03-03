# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20160302_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_time',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
    ]
