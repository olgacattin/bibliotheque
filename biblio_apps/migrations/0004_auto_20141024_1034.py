# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0003_auto_20141002_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_prop', models.CharField(max_length=150)),
                ('prenom_prop', models.CharField(max_length=150)),
                ('addr_prop', models.CharField(max_length=150, blank=True)),
                ('npa_prop', models.CharField(max_length=4)),
                ('city_prop', models.CharField(max_length=50)),
                ('phone_prop', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_table', models.CharField(max_length=10)),
                ('nom_table', models.CharField(max_length=30)),
                ('code_type', models.CharField(max_length=5)),
                ('nom_type', models.CharField(max_length=30)),
                ('code_pere', models.CharField(max_length=3, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Personne',
            new_name='Utilisateur',
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='type_prop',
            field=models.ForeignKey(related_name='proprietaire', to='biblio_apps.Types'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='pret',
            old_name='perso',
            new_name='utilisateur',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='prop_livre',
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='city_fourn',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='npa_fourn',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livre',
            name='monn_livre',
            field=models.ForeignKey(related_name='type_monnaie', null=True, blank=True, to='biblio_apps.Types'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livre',
            name='proprietaire',
            field=models.ForeignKey(default=1, to='biblio_apps.Proprietaire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livre',
            name='subtype_livre',
            field=models.ForeignKey(related_name='sub_type_livre', null=True, blank=True, to='biblio_apps.Types'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pret',
            name='date_prolong',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pret',
            name='date_rappel_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pret',
            name='date_rappel_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pret',
            name='date_rappel_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pret',
            name='date_reserv',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pret',
            name='date_reserv_utilis',
            field=models.ForeignKey(related_name='user_reservation',null=True, blank=True, to='biblio_apps.Utilisateur'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livre',
            name='cate_livre',
            field=models.ForeignKey(related_name='categorie', to='biblio_apps.Types'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 10, 24, 10, 33, 49, 910182), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='lang_livre',
            field=models.ForeignKey(related_name='langue', to='biblio_apps.Types'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='livre',
            name='type_livre',
            field=models.ForeignKey(related_name='type_livre', to='biblio_apps.Types'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 10, 24, 10, 33, 49, 912502)),
            preserve_default=True,
        ),
    ]
