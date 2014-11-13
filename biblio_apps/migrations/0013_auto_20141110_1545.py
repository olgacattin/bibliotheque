# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0012_auto_20141110_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_cate', models.CharField(max_length=5)),
                ('nom_cate', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ('code_cate', 'nom_cate'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_form', models.CharField(max_length=5)),
                ('nom_form', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ('code_form', 'nom_form'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_Langue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_lang', models.CharField(max_length=5)),
                ('nom_lang', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ('code_lang', 'nom_lang'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_Monnaie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_mone', models.CharField(max_length=5)),
                ('nom_mone', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ('code_mone', 'nom_mone'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_Proprietaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_prop', models.CharField(max_length=5)),
                ('nom_prop', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ('code_prop', 'nom_prop'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_SousCategorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_sous_cate', models.CharField(max_length=5)),
                ('nom_sous_cate', models.CharField(max_length=150, null=True, blank=True)),
                ('code_cate', models.ForeignKey(to='biblio_apps.Type_Categorie')),
            ],
            options={
                'ordering': ('code_cate', 'code_sous_cate', 'nom_sous_cate'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='livre',
            name='cate_livre',
            field=models.ForeignKey(to='biblio_apps.Type_Categorie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 45, 49, 998893), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='form_livre',
            field=models.ForeignKey(to='biblio_apps.Type_Format'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='lang_livre',
            field=models.ForeignKey(to='biblio_apps.Type_Langue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='monn_livre',
            field=models.ForeignKey(blank=True, to='biblio_apps.Type_Monnaie', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='subcate_livre',
            field=models.ForeignKey(default=1, to='biblio_apps.Type_SousCategorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 45, 50, 1312)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='type_prop',
            field=models.ForeignKey(to='biblio_apps.Type_Proprietaire'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
