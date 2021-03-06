# -*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

from django.db import models
from django.db.models import Q

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render, get_object_or_404

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from biblio_apps.models import Utilisateur

from biblio_apps.models import Auteur
from biblio_apps.models import Fournisseur
from biblio_apps.models import Livre
from biblio_apps.models import Pret
from biblio_apps.models import Proprietaire
from biblio_apps.models import TypeCategorie, TypeSousCategorie, TypeFormat, TypeProprietaire, TypeLangue, TypeMonnaie
from biblio_apps.models import Utilisateur

from forms import UtilisateurForm, AuteurForm, ProprietaireForm, FournisseurForm
from forms import TypeCategorieForm, TypeSousCategorieForm, TypeFormatForm, TypeProprietaireForm, TypeLangueForm, TypeMonnaieForm

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


def rappels_list(request):
    rappel_list = Pret.objects.filter(date_back_prev__lte=datetime.now())

    context = {'rappel_list' : rappel_list}
    return render(request, 'rappels_list.html', context)


def livres_pret_en_cours(request):
    livres_prets = Pret.objects.filter(Q(date_back_prev__lte=datetime.now()))

    return render(request, '', null)


#Gestion Utilisateur table.
class UtilisateurList(ListView):
    model = Utilisateur
    template_name = "utilisateur_list.html"
  
    def get_context_data(self, **kwargs):
        context = super(UtilisateurList, self).get_context_data(**kwargs)
        return context

class UtilisateurCreate(CreateView):
    model = Utilisateur
    template_name = "utilisateur_form.html"
    form_class = UtilisateurForm
    success_url = reverse_lazy('utilisateur_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class UtilisateurUpdate(UpdateView):
    model = Utilisateur
    template_name = "utilisateur_form.html"
    form_class = UtilisateurForm
    success_url = reverse_lazy('utilisateur_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Utilisateur, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def utilisateur_delete(request, util_id):
    utilisateur = get_object_or_404(Utilisateur, pk=util_id)
    success_url = reverse_lazy('utilisateur_list')

    lien_pret = Pret.objects.filter(utilisateur__id = util_id)

    if (lien_pret):
        messages.warning(request, 'Utilisateur est lié avec livre!')
    else:
        utilisateur.delete()
        messages.success(request, 'Utilisateur est effacé!')

    return HttpResponseRedirect(reverse_lazy('utilisateur_list'))


#Gestion Auteur table.
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
    
@require_POST
def auteur_delete(request, auteur_id):
    auteur = get_object_or_404(Auteur, pk=auteur_id)
    success_url = reverse_lazy('auteur_list')

    lien_livre = Livre.objects.filter(auteurs__id = auteur_id)

    if (lien_livre):
        messages.warning(request, 'Auteur est lié avec livre!')
    else:
        auteur.delete()
        messages.success(request, 'Auteur est effacé!')

    return HttpResponseRedirect(reverse_lazy('auteur_list'))


#Gestion Propriétaire table.
class ProprietaireList(ListView):
    model = Proprietaire
    template_name = "proprietaire_list.html"
  
    def get_context_data(self, **kwargs):
        context = super(ProprietaireList, self).get_context_data(**kwargs)
        return context

class ProprietaireCreate(CreateView):
    model = Proprietaire
    template_name = "proprietaire_form.html"
    form_class = ProprietaireForm
    success_url = reverse_lazy('proprietaire_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class ProprietaireUpdate(UpdateView):
    model = Proprietaire
    template_name = "proprietaire_form.html"
    form_class = ProprietaireForm
    success_url = reverse_lazy('proprietaire_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Proprietaire, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def proprietaire_delete(request, prop_id):
    proprietaire = get_object_or_404(Proprietaire, pk=prop_id)
    success_url = reverse_lazy('proprietaire_list')

    lien_livre = Livre.objects.filter(proprietaire__id = prop_id)

    if (lien_livre):
        messages.warning(request, 'Proprietaire est lié avec livre!')
    else:
        proprietaire.delete()
        messages.success(request, 'Proprietaire est effacé!')

    return HttpResponseRedirect(reverse_lazy('proprietaire_list'))


#Gestion Fournisseur table.
class FournisseurList(ListView):
    model = Fournisseur
    template_name = "fournisseur_list.html"
  
    def get_context_data(self, **kwargs):
        context = super(FournisseurList, self).get_context_data(**kwargs)
        return context

class FournisseurCreate(CreateView):
    model = Fournisseur
    template_name = "fournisseur_form.html"
    form_class = FournisseurForm
    success_url = reverse_lazy('fournisseur_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class FournisseurUpdate(UpdateView):
    model = Fournisseur
    template_name = "fournisseur_form.html"
    form_class = FournisseurForm
    success_url = reverse_lazy('fournisseur_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Fournisseur, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def fournisseur_delete(request, fourn_id):
    fournisseur = get_object_or_404(Fournisseur, pk=fourn_id)
    success_url = reverse_lazy('fournisseur_list')

    lien_livre = Livre.objects.filter(fournisseur__id = fourn_id)

    if (lien_livre):
        messages.warning(request, 'Fournisseur est lié avec livre!')
    else:
        fournisseur.delete()
        messages.success(request, 'Fournisseur est effacé!')

    return HttpResponseRedirect(reverse_lazy('fournisseur_list'))



#Gestion Catégorie type table.
class TypeCategorieList(ListView):
    model = TypeCategorie
    template_name = "type_categorie_list.html"

    def get_context_data(self, **kwargs):
        context = super(TypeCategorieList, self).get_context_data(**kwargs)
        return context


class TypeCategorieCreate(CreateView):
    model = TypeCategorie
    template_name = "type_categorie_form.html"
    form_class = TypeCategorieForm
    success_url = reverse_lazy('type_categorie_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class TypeCategorieUpdate(UpdateView):
    model = TypeCategorie
    template_name = "type_categorie_form.html"
    form_class = TypeCategorieForm
    success_url = reverse_lazy('type_categorie_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(TypeCategorie, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def type_categorie_delete(request, type_cate_id):
    type_categorie = get_object_or_404(TypeCategorie, pk=type_cate_id)
    success_url = reverse_lazy('type_categorie_list')

    lien_livre = Livre.objects.filter(cate_livre__id = type_cate_id)

    if (lien_livre):
        messages.warning(request, 'Type Catégorie est lié avec livre!')
    else:
        type_categorie.delete()
        messages.success(request, 'Type Catégorie est effacé!')

    return HttpResponseRedirect(reverse_lazy('type_categorie_list'))


#Gestion Sous_Catégorie type table.
class TypeSousCategorieList(ListView):
    model = TypeSousCategorie
    template_name = "type_sous_categorie_list.html"

    def get_context_data(self, **kwargs):
        context = super(TypeSousCategorieList, self).get_context_data(**kwargs)
        return context


class TypeSousCategorieCreate(CreateView):
    model = TypeSousCategorie
    template_name = "type_sous_categorie_form.html"
    form_class = TypeSousCategorieForm
    success_url = reverse_lazy('type_sous_categorie_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class TypeSousCategorieUpdate(UpdateView):
    model = TypeSousCategorie
    template_name = "type_sous_categorie_form.html"
    form_class = TypeSousCategorieForm
    success_url = reverse_lazy('type_sous_categorie_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(TypeSousCategorie, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def type_sous_categorie_delete(request, type_sous_cate_id):
    type_categorie = get_object_or_404(TypeSousCategorie, pk=type_sous_cate_id)
    success_url = reverse_lazy('type_categorie_list')

    lien_livre = Livre.objects.filter(cate_sous_livre__id = type_sous_cate_id)

    if (lien_livre):
        messages.warning(request, 'Type Sous-Catégorie est lié avec livre!')
    else:
        type_categorie.delete()
        messages.success(request, 'Type Sous-Catégorie est effacé!')

    return HttpResponseRedirect(reverse_lazy('type_sous_categorie_list'))


#Gestion Format type table.
class TypeFormatList(ListView):
    model = TypeFormat
    template_name = "type_format_list.html"

    def get_context_data(self, **kwargs):
        context = super(TypeFormatList, self).get_context_data(**kwargs)
        return context


class TypeFormatCreate(CreateView):
    model = TypeFormat
    template_name = "type_format_form.html"
    form_class = TypeFormatForm
    success_url = reverse_lazy('type_format_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class TypeFormatUpdate(UpdateView):
    model = TypeFormat
    template_name = "type_format_form.html"
    form_class = TypeFormatForm
    success_url = reverse_lazy('type_format_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(TypeFormat, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def type_format_delete(request, type_format_id):
    type_format = get_object_or_404(TypeFormat, pk=type_format_id)
    success_url = reverse_lazy('type_format_list')

    lien_livre = Livre.objects.filter(form_livre__id = type_format_id)

    if (lien_livre):
        messages.warning(request, 'Type format est lié avec livre!')
    else:
        type_format.delete()
        messages.success(request, 'Type format est effacé!')

    return HttpResponseRedirect(reverse_lazy('type_format_list'))

#Gestion Propriétaire type table.
class TypeProprietaireList(ListView):
    model = TypeProprietaire
    template_name = "type_proprietaire_list.html"

    def get_context_data(self, **kwargs):
        context = super(TypeProprietaireList, self).get_context_data(**kwargs)
        return context


class TypeProprietaireCreate(CreateView):
    model = TypeProprietaire
    template_name = "type_proprietaire_form.html"
    form_class = TypeProprietaireForm
    success_url = reverse_lazy('type_proprietaires_list')
    

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class TypeProprietaireUpdate(UpdateView):
    model = TypeProprietaire
    template_name = "type_proprietaire_form.html"
    form_class = TypeProprietaireForm
    success_url = reverse_lazy('type_proprietaire_list')
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(TypeProprietaire, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def type_proprietaire_delete(request, type_prop_id):
    type_proprietaire = get_object_or_404(TypeProprietaire, pk=type_prop_id)
    success_url = reverse_lazy('type_proprietaire_list')

    lien_prop = Proprietaire.objects.filter(type_prop__id = type_prop_id)

    if (lien_prop):
        messages.warning(request, 'Type proprietaire est lié avec livre!')
    else:
        type_proprietaire.delete()
        messages.success(request, 'Type proprietaire est effacé!')

    return HttpResponseRedirect(reverse_lazy('type_proprietaire_list'))


#Gestion Langue type table.
class TypeLangueList(ListView):
    model = TypeLangue
    template_name = "type_langue_list.html"

    def get_context_data(self, **kwargs):
        context = super(TypeLangueList, self).get_context_data(**kwargs)
        return context


class TypeLangueCreate(CreateView):
    model = TypeLangue
    template_name = "type_langue_form.html"
    form_class = TypeLangueForm
    success_url = reverse_lazy('type_langue_list')
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class TypeLangueUpdate(UpdateView):
    model = TypeLangue
    template_name = "type_langue_form.html"
    form_class = TypeLangueForm
    success_url = reverse_lazy('type_langue_list')
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(TypeLangue, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def type_langue_delete(request, type_lang_id):
    type_langue = get_object_or_404(TypeLangue, pk=type_lang_id)
    success_url = reverse_lazy('type_langue_list')

    lien_livre = Livre.objects.filter(lang_livre__id = type_lang_id)

    if (lien_livre):
        messages.warning(request, 'Type langue est lié avec livre!')
    else:
        type_langue.delete()
        messages.success(request, 'Type langue est effacé!')

    return HttpResponseRedirect(reverse_lazy('type_langue_list'))



#Gestion Monnaie type table.
class TypeMonnaieList(ListView):
    model = TypeMonnaie
    template_name = "type_monnaie_list.html"

    def get_context_data(self, **kwargs):
        context = super(TypeMonnaieList, self).get_context_data(**kwargs)
        return context


class TypeMonnaieCreate(CreateView):
    model = TypeMonnaie
    template_name = "type_monnaie_form.html"
    form_class = TypeMonnaieForm
    success_url = reverse_lazy('type_monnaie_list')
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    

class TypeMonnaieUpdate(UpdateView):
    model = TypeMonnaie
    template_name = "type_monnaie_form.html"
    form_class = TypeMonnaieForm
    success_url = reverse_lazy('type_monnaie_list')
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(TypeMonnaie, pk=pk)

    def form_valid(self, form):
        self.object = form.save()    

        return HttpResponseRedirect(self.get_success_url())
    
@require_POST
def type_monnaie_delete(request, type_monn_id):
    type_monnaie = get_object_or_404(TypeMonnaie, pk=type_monn_id)
    success_url = reverse_lazy('type_monnaie_list')

    lien_livre = Livre.objects.filter(monn_livre__id = type_monn_id)

    if (lien_livre):
        messages.warning(request, 'Type monnaie est lié avec livre!')
    else:
        type_monnaie.delete()
        messages.success(request, 'Type monnaie est effacé!')

    return HttpResponseRedirect(reverse_lazy('type_monnaie_list'))






