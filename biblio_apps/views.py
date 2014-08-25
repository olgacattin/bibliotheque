from django.http import Http404
from django.shortcuts import render

from biblio_apps.models import Livre
from biblio_apps.models import Auteur

def index(request):
    auteur_list = Auteur.objects.order_by('-nom_auteur')[:7]
    context = {'auteur_list': auteur_list}

    return render(request, 'index.html', context)

def livres_list(request):
    livre_list = Livre.objects.order_by('-code_livre')[:7]
    context = {'livre_list': livre_list}
 
    return render(request, 'livres_list.html', context)

def detail(request, livre_id):
    try:
        livre = Livre.objets.get(pk=livre_id)
    except Livre.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'livre': livre})

