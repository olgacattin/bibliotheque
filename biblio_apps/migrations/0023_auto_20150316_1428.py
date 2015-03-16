# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0022_auto_20150316_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 14, 28, 18, 174315), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 14, 28, 18, 176831)),
            preserve_default=True,
        ),
    ]
