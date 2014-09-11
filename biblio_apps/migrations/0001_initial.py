# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_auteur', models.CharField(max_length=100)),
                ('prenom_auteur', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre_livre', models.CharField(max_length=60)),
                ('cate_livre', models.CharField(max_length=5)),
                ('code_livre', models.CharField(max_length=3)),
                ('nom_livre', models.CharField(max_length=100)),
                ('type_livre', models.CharField(max_length=4, choices=[(b'MATH', b'Mathematiques'), (b'PROG', b'Programmation'), (b'BDON', b'Base de donn\xc3\xa9es'), (b'ALGO', b'Algorithmique'), (b'FINA', b'Finances'), (b'MARK', b'Marketing'), (b'DIVS', b'Divers')])),
                ('edit_livre', models.CharField(max_length=50, blank=True)),
                ('class_livre', models.CharField(max_length=10, blank=True)),
                ('lang_livre', models.CharField(max_length=3, choices=[(b'FR', b'Fran\xc3\xa7ais'), (b'ALL', b'Allemand'), (b'ANG', b'Anglais'), (b'ITA', b'Italiano')])),
                ('annee_livre', models.CharField(max_length=10, blank=True)),
                ('isbn_livre', models.CharField(max_length=50, blank=True)),
                ('prix_livre', models.DecimalField(max_digits=6, decimal_places=2)),
                ('prop_livre', models.CharField(max_length=100, blank=True)),
                ('disp_livre', models.BooleanField(default=True)),
                ('auteurs', models.ManyToManyField(to='biblio_apps.Auteur')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('postcode', models.CharField(default=b'', max_length=12)),
                ('city', models.CharField(default=b'', max_length=50)),
                ('phone_prive', models.CharField(max_length=50, blank=True)),
                ('phone_prof', models.CharField(max_length=50, blank=True)),
                ('phone_mobil', models.CharField(max_length=50, blank=True)),
                ('phone_fax', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_pret', models.DateField()),
                ('date_back_prev', models.DateField()),
                ('date_back_pret', models.DateField()),
                ('livre', models.ForeignKey(to='biblio_apps.Livre')),
                ('perso', models.ForeignKey(to='biblio_apps.Personne')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
