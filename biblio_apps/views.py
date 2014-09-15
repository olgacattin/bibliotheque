from django.http import Http404
from django.shortcuts import render
from django.db import models
from django.db.model import Q

from biblio_apps.models import Livre
from biblio_apps.models import Auteur
from biblio_apps.models import Pret
from biblio_apps.models import Personne

from datetime import datetime

def index(request):
    auteur_list = Auteur.objects.order_by('-nom_auteur')[:7]
    context = {'auteur_list': auteur_list}

    return render(request, 'index.html', context)


def livres_list(request):
   #import pdb; pdb.set_trace() 

    pret_livre = Pret.objects.get(Q(date_back_pret__gte=datetime.now()) | Q(date_back_pret__isnull=True))
    livre_pret = Livre.objects.filter(pk__in=[pret_livre.livre_id]).update(disp_livre=False)
    livre_list = Livre.objects.all().select_related('Pret')
    
    #livres_prets = Livre.objects.filter(pk__in=['livre', pret.get('livre')) for pret in pret_livre]).update(disp_livre=false)
    #livres_prets = Livre_list.filter(pk__in=['livre', pret.get('livre')) for pret in pret_livre]).update(disp_livre=false)

    context = {'livre_list': livre_list}
 
    return render(request, 'livres_list.html', context)


def livres_detail(request, livre_id):
    try:
        livre = Livre.objets.get(pk=livre_id)
    except Livre.DoesNotExist:
        raise Http404

    return render(request, 'livres_detail.html', {'livre': livre})


def prets_list(request):
    pret_list = Pret.objects.select_related('livre', 'perso')
    context = {'pret_list': pret_list}

    return render(request, 'prets_list.html', context)


def personnes_list(request):
    personne_list = Personne.objects.order_by('-last_name')[:7]
    context = {'personne_list': personne_list}

    return render(request, 'personnes_list.html', context)



def rappels_list(request):
    rappel_list = Pret.objects.filter(date_back_prev__ge=datetime.now())
    context = {'rappel_list' : rappel_list}
    
    return render(request, 'prets_list.html', context)


def livres_pret_en_cours(request):
    livres_prets = Pret.objects.filter(date_back_pret=isnull)

    return render(request, '', null)
    

def detail(request, livre_id):
    try:
        livre = Livre.objets.get(pk=livre_id)
    except Livre.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'livre': livre})

