# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_fourn', models.CharField(max_length=150)),
                ('addr_fourn', models.CharField(max_length=150, blank=True)),
                ('phone_fourn', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2014, 9, 18, 14, 51, 14, 817257), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livre',
            name='fournisseur',
            field=models.ForeignKey(default=1, to='biblio_apps.Fournisseur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_back_pret',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2014, 9, 18, 14, 51, 14, 822894)),
        ),
    ]
