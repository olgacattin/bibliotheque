# -*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponseRedirect

from django.db import models
from django.db.models import Q

from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render, get_object_or_404

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from biblio_apps.models import Auteur
from biblio_apps.models import Fournisseur
from biblio_apps.models import Livre
from biblio_apps.models import Pret
from biblio_apps.models import Proprietaire
from biblio_apps.models import Types
from biblio_apps.models import Utilisateur

from forms import AuteurForm 

from datetime import datetime
#import pdb; pdb.set_trace()

def index(request):
    return render(request, 'index.html', None)

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


def utilisateurs_list(request):
    utilisateur_list = Utilisateur.objects.order_by('-last_name')[:7]

    context = {'utilisateur_list': utilisateur_list}
    return render(request, 'utilisateurs_list.html', context)


def utilisateur_detail(request, utilisateur_id):

    try:
        #import pdb; pdb.set_trace()
        utilisateur = Utilisateur.objects.get(pk=utilisateur_id)
        context = {'utilisateur': utilisateur}

    except Personne.DoesNotExist:
       raise Http404

    return render(request, 'utilisateur_detail.html', context)


def utilisateur_edition(request):
    utilisateur = utilisateur()
    
    utilisateur.save()
    return render(request, 'utilisateur_edition.html', None)


def rappels_list(request):
    rappel_list = Pret.objects.filter(date_back_prev__lte=datetime.now())

    context = {'rappel_list' : rappel_list}
    return render(request, 'rappels_list.html', context)


def livres_pret_en_cours(request):
    livres_prets = Pret.objects.filter(Q(date_back_prev__lte=datetime.now()))

    return render(request, '', null)

    
def auteurs_list(request):
    auteurs_list = Auteur.objects.all()

    context = {'auteurs_list': auteurs_list}
    return render(request, 'auteurs_list.html', context)


def auteur_modify(request, auteur_id):
    return render(request, 'auteur_modify.html', context)

def auteur_delete(request, auteur_id):
    return render(request, 'auteur_delete_html', context)


def auteur_edition(request, auteur_id):
    #import pdb; pdb.set_trace()
    
    #if request.method == 'POST':
    auteur = Auteur.objects.get(pk = auteur_id)
    form = AuteurForm(request.POST or None, instance = auteur)

    if form.is_valid():
        nom = form.cleaned_data['nom_auteur']
        prenom.form.cleaned_data['prenom_auteur']

        auteur = form.save()
        auteur.save()
        #return HttpResponseRedirect('biblio_apps/auteurs_list/')
        return redirect(auteurs_list)

    #else:
    #    form = AuteurForm()

    context = {'auteur_edition_form' : form}
    return render(request, 'auteur_edition.html', context)


def fournisseurs_list(request):
    fournisseurs_list = Fournisseur.objects.all()

    context = {'fournisseurs_list': fournisseurs_list}
    return render(request, 'fournisseurs_list.html', context)



# Gestion Auteur table.
class AuteurList(ListView):
    model = Auteur
    template_name = "auteur_list.html"
  
    def get_context_data(self, **kwargs):
        context = super(AuteurList, self).get_context_data(**kwargs)
        return context

class AuteurCreate(CreateView):
    model = Auteur
    template_name = "auteur_form.html"
    form_class = AuteurForm
    success_url = reverse_lazy('auteur_list')

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class AuteurUpdate(UpdateView):
    model = Auteur
    template_name = "auteur_form.html"
    form_class = AuteurForm
    success_url = reverse_lazy('auteur_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Auteur, pk=pk)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class AuteurDelete(DeleteView):
    model = Auteur
    template_name = "auteur_delete.html"
    form_class = AuteurForm
    success_url = reverse_lazy('auteur_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Auteur, pk=pk)



