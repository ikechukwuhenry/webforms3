# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywikipedia', '0003_auto_20170113_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=b'1234', max_length=20),
        ),
    ]
