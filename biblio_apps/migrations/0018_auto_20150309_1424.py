# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0017_auto_20150309_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typecategorie',
            options={},
        ),
        migrations.AlterModelOptions(
            name='typesouscategorie',
            options={'ordering': ('categorie', 'nom_sous_cate')},
        ),
        migrations.RenameField(
            model_name='typesouscategorie',
            old_name='code_cate',
            new_name='categorie',
        ),
        migrations.RemoveField(
            model_name='typecategorie',
            name='code_cate',
        ),
        migrations.RemoveField(
            model_name='typesouscategorie',
            name='code_sous_cate',
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2015, 3, 9, 14, 24, 27, 126193), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2015, 3, 9, 14, 24, 27, 128694)),
            preserve_default=True,
        ),
    ]
