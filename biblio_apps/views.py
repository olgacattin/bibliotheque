# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.db import models
from django.db.models import Q

from biblio_apps.models import Livre
from biblio_apps.models import Auteur
from biblio_apps.models import Pret
from biblio_apps.models import Personne
from biblio_apps.models import Fournisseur

from datetime import datetime
#import pdb; pdb.set_trace()

def index(request):
    auteur_list = Auteur.objects.order_by('-nom_auteur')[:7]

    context = {'auteur_list': auteur_list}
    return render(request, 'index.html', context)

def livres_list(request):
    livre_list = Livre.objects.all()			#Liste de tous les livres

    #Liste de tous les prêts en cours
    prets_en_cours = Pret.objects.filter(Q(date_back_prev__lte=datetime.now()) | Q(date_back_pret__isnull=True))

    if prets_en_cours:        # Liste avec données
        prets_actifs =[]

        for pret in prets_en_cours:
            prets_actifs.append(pret.livre_id)
   
        for livre in livre_list:
            livre.disp_livre = not livre.pk in prets_actifs

    context = {'livre_list': livre_list}
    return render(request, 'livres_list.html', context)


def livres_detail(request, livre_id):

    #import pdb; pdb.set_trace()
    try:
        livre = Livre.objects.select_related('auteurs', 'fournisseur').get(pk=livre_id)
        auteurs_livre = livre.auteurs.all()
        print(auteurs_livre)
        context =  {'livre': livre}

    except Livre.DoesNotExist:
        raise Http404

    return render(request, 'livres_detail.html', context)


def prets_list(request):
    pret_list = Pret.objects.select_related('livre', 'perso')

    context = {'pret_list': pret_list}
    return render(request, 'prets_list.html', context)


def personnes_list(request):
    personne_list = Personne.objects.order_by('-last_name')[:7]

    context = {'personne_list': personne_list}
    return render(request, 'personnes_list.html', context)


def rappels_list(request):
    rappel_list = Pret.objects.filter(date_back_prev__lte=datetime.now())

    context = {'rappel_list' : rappel_list}
    return render(request, 'rappels_list.html', context)


def livres_pret_en_cours(request):
    livres_prets = Pret.objects.filter(Q(date_back_prev__lte=datetime.now()))

    return render(request, '', null)
    

def detail(request, livre_id):
    try:
        livre = Livre.objets.get(pk=livre_id)
    except Livre.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'livre': livre})

