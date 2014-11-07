# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0010_auto_20141106_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='subtype_livre',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='type_livre',
        ),
        migrations.AddField(
            model_name='livre',
            name='ean13_livre',
            field=models.CharField(default=1, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livre',
            name='form_livre',
            field=models.ForeignKey(related_name='format', default=1, to='biblio_apps.Types'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livre',
            name='subcate_livre',
            field=models.ForeignKey(related_name='sub_categorie', blank=True, to='biblio_apps.Types', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 11, 7, 12, 23, 25, 410466), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 11, 7, 12, 23, 25, 412879)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='types',
            name='nom_type',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
