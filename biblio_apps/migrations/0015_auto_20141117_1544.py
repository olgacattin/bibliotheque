# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0014_auto_20141110_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='cate_livre',
            field=models.ForeignKey(to='biblio_apps.TypeCategorie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 11, 17, 15, 44, 48, 922281), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='form_livre',
            field=models.ForeignKey(to='biblio_apps.TypeFormat'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='lang_livre',
            field=models.ForeignKey(to='biblio_apps.TypeLangue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='monn_livre',
            field=models.ForeignKey(blank=True, to='biblio_apps.TypeMonnaie', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 11, 17, 15, 44, 48, 924772)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='type_prop',
            field=models.ForeignKey(to='biblio_apps.TypeProprietaire'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='typesouscategorie',
            name='code_cate',
            field=models.ForeignKey(to='biblio_apps.TypeCategorie'),
            preserve_default=True,
        ),
    ]
