# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywikipedia', '0004_auto_20170114_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=250)),
                ('reporter', models.CharField(max_length=250)),
            ],
        ),
    ]
