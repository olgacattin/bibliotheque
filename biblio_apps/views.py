from django.http import Http404
from django.shortcuts import render

from biblio_apps.models import Livre
from biblio_apps.models import Auteur
from biblio_apps.models import Pret
from biblio_apps.models import Personne

def index(request):
    auteur_list = Auteur.objects.order_by('-nom_auteur')[:7]
    context = {'auteur_list': auteur_list}

    return render(request, 'index.html', context)

def livres_list(request):
    livre_list = Livre.objects.order_by('-code_livre')[:7]
    context = {'livre_list': livre_list}
 
    return render(request, 'livres_list.html', context)

def livres_detail(request, livre_id):
    try:
        livre = Livre.objets.get(pk=livre_id)
    except Livre.DoesNotExist:
        raise Http404
    return render(request, 'livres_detail.html', {'livre': livre})

def prets_list(request):
#    pret_list = Pret.objects.order_by('-date_pret')[:7]
    pret_list = Pret.objects.select_related('id_livre', 'id_perso')
    context = {'pret_list': pret_list}

    return render(request, 'prets_list.html', context)

def personnes_list(request):
    personne_list = Personne.objects.order_by('-last_name')[:7]
    context = {'personne_list': personne_list}

    return render(request, 'personnes_list.html', context)

def detail(request, livre_id):
    try:
        livre = Livre.objets.get(pk=livre_id)
    except Livre.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'livre': livre})

