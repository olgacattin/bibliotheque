# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0005_auto_20141024_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 10, 24, 17, 16, 22, 855841), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='fournisseur',
            field=models.ForeignKey(to='biblio_apps.Fournisseur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='proprietaire',
            field=models.ForeignKey(to='biblio_apps.Proprietaire'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 10, 24, 17, 16, 22, 858203)),
            preserve_default=True,
        ),
    ]
