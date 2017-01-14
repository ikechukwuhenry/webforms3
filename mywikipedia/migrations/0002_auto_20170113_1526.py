# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mywikipedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default=datetime.datetime(2017, 1, 13, 15, 26, 8, 145847, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default=datetime.datetime(2017, 1, 13, 15, 26, 49, 496904, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
