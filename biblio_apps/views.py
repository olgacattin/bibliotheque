from django.http import Http404
from django.shortcuts import render

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
    livre_list = Livre.objects.order_by('titre_livre')
    livre_prets = Pret.objects.filter(date_back_pret=None)

    #for pret in livre_prets:
     #   print pret.date_back_pret


    livre_list2 = Livre.objects.filter(livre_id__in=[livre_prets]
    
    #for livre in livre_list2:
     #   print livre.disp_livre

#import pdb; pdb.set_trace()
    #for livre in livre_list:
     #   livre.disp_livre = False
    
    #livres_prets = Livre.objects.filter(pk__in=['livre', pret.get('livre')) for pret in livres_prets]).update(disp_livre=false)

    #for pret in livres_prets:
    #    dispo_list.add(pret.id_livre)
    #    livre_list.disp_livre = false
        	
    #livre_list = Livre.objects.all().pret_set.all()
    #livre_list = livre_list.pret_set.all() 

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

