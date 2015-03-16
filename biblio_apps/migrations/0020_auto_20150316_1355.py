# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_apps', '0019_auto_20150316_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_edit', models.CharField(max_length=150)),
                ('addr_edit', models.CharField(max_length=150, blank=True)),
                ('npa_edit', models.CharField(max_length=4)),
                ('city_edit', models.CharField(max_length=50)),
                ('phone_edit', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_acqui',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 13, 55, 43, 15435), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 13, 55, 43, 17887)),
            preserve_default=True,
        ),
    ]
