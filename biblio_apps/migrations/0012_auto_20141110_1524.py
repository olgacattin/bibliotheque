# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0011_auto_20141107_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='types',
            options={'ordering': ('nom_table', 'nom_type')},
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 24, 5, 61367), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 24, 5, 65385)),
            preserve_default=True,
        ),
    ]
