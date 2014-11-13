# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0013_auto_20141110_1545'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type_Langue',
            new_name='TypeCategorie',
        ),
        migrations.RenameModel(
            old_name='Type_Proprietaire',
            new_name='TypeFormat',
        ),
        migrations.RenameModel(
            old_name='Type_Monnaie',
            new_name='TypeLangue',
        ),
        migrations.RenameModel(
            old_name='Type_Format',
            new_name='TypeMonnaie',
        ),
        migrations.RenameModel(
            old_name='Type_Categorie',
            new_name='TypeProprietaire',
        ),
        migrations.RenameModel(
            old_name='Type_SousCategorie',
            new_name='TypeSousCategorie',
        ),
        migrations.AlterModelOptions(
            name='typecategorie',
            options={'ordering': ('code_cate', 'nom_cate')},
        ),
        migrations.AlterModelOptions(
            name='typeformat',
            options={'ordering': ('code_form', 'nom_form')},
        ),
        migrations.AlterModelOptions(
            name='typelangue',
            options={'ordering': ('code_lang', 'nom_lang')},
        ),
        migrations.AlterModelOptions(
            name='typemonnaie',
            options={'ordering': ('code_mone', 'nom_mone')},
        ),
        migrations.AlterModelOptions(
            name='typeproprietaire',
            options={'ordering': ('code_prop', 'nom_prop')},
        ),
        migrations.RenameField(
            model_name='typecategorie',
            old_name='code_lang',
            new_name='code_cate',
        ),
        migrations.RenameField(
            model_name='typecategorie',
            old_name='nom_lang',
            new_name='nom_cate',
        ),
        migrations.RenameField(
            model_name='typeformat',
            old_name='code_prop',
            new_name='code_form',
        ),
        migrations.RenameField(
            model_name='typeformat',
            old_name='nom_prop',
            new_name='nom_form',
        ),
        migrations.RenameField(
            model_name='typelangue',
            old_name='code_mone',
            new_name='code_lang',
        ),
        migrations.RenameField(
            model_name='typelangue',
            old_name='nom_mone',
            new_name='nom_lang',
        ),
        migrations.RenameField(
            model_name='typemonnaie',
            old_name='code_form',
            new_name='code_mone',
        ),
        migrations.RenameField(
            model_name='typemonnaie',
            old_name='nom_form',
            new_name='nom_mone',
        ),
        migrations.RenameField(
            model_name='typeproprietaire',
            old_name='code_cate',
            new_name='code_prop',
        ),
        migrations.RenameField(
            model_name='typeproprietaire',
            old_name='nom_cate',
            new_name='nom_prop',
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 53, 5, 319976), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 53, 5, 322380)),
            preserve_default=True,
        ),
    ]
