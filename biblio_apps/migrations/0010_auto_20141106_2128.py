# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0009_auto_20141030_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auteur',
            options={'ordering': ('nom_auteur', 'prenom_auteur')},
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 11, 6, 21, 28, 33, 308210), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 11, 6, 21, 28, 33, 310538)),
            preserve_default=True,
        ),
    ]
