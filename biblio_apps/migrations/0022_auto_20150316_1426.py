# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0021_auto_20150316_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='editeur',
            field=models.ForeignKey(default=1, to='biblio_apps.Editeur'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 14, 26, 37, 475380), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 14, 26, 37, 477876)),
            preserve_default=True,
        ),
    ]
