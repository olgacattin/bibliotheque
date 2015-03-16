# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime 

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Model(table): TypeCatégorie
class TypeCategorie(models.Model):
    nom_cate = models.CharField(max_length = 150, null = True, blank = True)

    def __unicode__(self):
        return u'%s' % self.nom_cate

    def get_values(self):
        values = self.all()
        return values

# Model(table): TypeSousCatégorie
class TypeSousCategorie(models.Model):
    nom_sous_cate = models.CharField(max_length = 150, null = True, blank = True)
    categorie = models.ForeignKey(TypeCategorie)

    def __unicode__(self):
        return u'%s' %  self.nom_sous_cate

    class Meta:
        ordering = ('categorie', 'nom_sous_cate')


# Model(table): TypeFormat
class TypeFormat(models.Model):
    code_form = models.CharField(max_length = 5, null = False, blank = False)
    nom_form = models.CharField(max_length = 150, null = True, blank = True)

    def __unicode__(self):
        return self.nom_form

    class Meta:
        ordering = ('code_form', 'nom_form')


# Model(table): TypePropriétaire
class TypeProprietaire(models.Model):
    code_prop = models.CharField(max_length = 5, null = False, blank = False)
    nom_prop = models.CharField(max_length = 150, null = True, blank = True)

    def __unicode__(self):
        return self.nom_prop

    class Meta:
        ordering = ('code_prop', 'nom_prop')


# Model(table): TypeLangue
class TypeLangue(models.Model):
    code_lang = models.CharField(max_length = 5, null = False, blank = False)
    nom_lang = models.CharField(max_length = 150, null = True, blank = True)

    def __unicode__(self):
        return self.nom_lang

    class Meta:
        ordering = ('code_lang', 'nom_lang')


# Model(table): TypeMonnaie
class TypeMonnaie(models.Model):
    code_mone = models.CharField(max_length = 5, null = False, blank = False)
    nom_mone = models.CharField(max_length = 150, null = True, blank = True)

    def __unicode__(self):
        return self.code_mone

    class Meta:
        ordering = ('code_mone', 'nom_mone')


# Model(table): Auteur
class Auteur(models.Model):
    nom_auteur = models.CharField(max_length = 100, blank = False)
    prenom_auteur = models.CharField(max_length = 100, blank = True)
	
    def __unicode__(self):
        return self.nom_auteur + " " + self.prenom_auteur
    
    def get_absolute_url(self):
        return reverse('auteur_detail', kwargs={'pk': self.pk})
   
    class Meta:
        ordering = ('nom_auteur', 'prenom_auteur')


# Model(table): Fournisseur
class Fournisseur(models.Model):
    nom_fourn = models.CharField(max_length = 150, blank = False)
    addr_fourn = models.CharField(max_length = 150, blank = True)
    npa_fourn = models.CharField(max_length = 4)
    city_fourn = models.CharField(max_length = 50)
    phone_fourn = models.CharField(max_length = 50, blank = True)

    def __unicode__(self):
        return self.nom_fourn + " - " + self.city_fourn


# Model(table): Editeur
class Editeur(models.Model):
    nom_edit = models.CharField(max_length = 150, blank = False)
    addr_edit = models.CharField(max_length = 150, blank = True)
    npa_edit = models.CharField(max_length = 4)
    city_edit = models.CharField(max_length = 50)
    phone_edit = models.CharField(max_length = 50, blank = True)

    def __unicode__(self):
        return self.nom_edit + " - " + self.city_edit


# Model(table): Proprietaire
class Proprietaire(models.Model):
    nom_prop = models.CharField(max_length = 150, blank = False)
    prenom_prop = models.CharField(max_length = 150, blank = False)
    addr_prop = models.CharField(max_length = 150, blank = True)
    npa_prop = models.CharField(max_length = 4)
    city_prop = models.CharField(max_length = 50)
    phone_prop = models.CharField(max_length = 50, blank = True)
    type_prop = models.ForeignKey(TypeProprietaire)

    def __unicode__(self):
       return self.nom_prop + " " + self.prenom_prop


# Model(table): Livre
class Livre(models.Model):

    titre_livre = models.CharField(max_length = 60, blank = False)
    form_livre = models.ForeignKey(TypeFormat)
    code_livre = models.CharField(max_length = 3, blank = False)
    nom_livre = models.CharField(max_length = 100, blank = False)
    cate_livre = models.ForeignKey(TypeCategorie)
    subcate_livre = models.ForeignKey(TypeSousCategorie)
    edit_livre = models.CharField(max_length = 50, blank = True)
    class_livre = models.CharField(max_length = 10, blank = True)
    lang_livre = models.ForeignKey(TypeLangue)
    annee_livre	= models.CharField(max_length = 10, blank = True)
    isbn_livre = models.CharField(max_length = 50, blank = True)
    ean13_livre = models.CharField(max_length = 50, blank = True)
    prix_livre = models.DecimalField(max_digits = 6, decimal_places = 2)
    monn_livre = models.ForeignKey(TypeMonnaie, null=True, blank=True)
    disp_livre = models.BooleanField(default = True)
    date_acqui = models.DateField(default = datetime.now(), null = True, blank = True)
    fournisseur = models.ForeignKey(Fournisseur)
    editeur = models.ForeignKey(Editeur)
    proprietaire = models.ForeignKey(Proprietaire)
    auteurs = models.ManyToManyField(Auteur)

    def __unicode__(self):
        return self.nom_livre + " " + self.isbn_livre + " " + self.annee_livre
  

# Model(table): Utilisateur
class Utilisateur(User):
    # firstname, lastname and email are defined in the User model 
    address	= models.CharField(max_length = 255, blank = True)
    postcode = models.CharField(max_length = 12, default = '')
    city = models.CharField(max_length = 50, default = '')
    phone_prive	= models.CharField(max_length = 50, blank = True)
    phone_prof = models.CharField(max_length = 50, blank = True)
    phone_mobil = models.CharField(max_length = 50, blank = True)
    phone_fax = models.CharField(max_length = 50, blank = True)

    class Meta:
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        if self.first_name or self.last_name:
            return u" ".join([self.first_name, self.last_name])
        else:
            return self.username


# Model(table): Pret
class Pret(models.Model):
    livre = models.ForeignKey(Livre)
    utilisateur = models.ForeignKey(Utilisateur)
    date_pret = models.DateField(default = datetime.now())
    date_back_prev = models.DateField()
    date_back_pret = models.DateField(null = True, blank = True)
    date_reserv = models.DateField(null = True, blank = True)
    date_reserv_utilis = models.ForeignKey(Utilisateur,null = True, blank = True, related_name = 'user_reservation')
    date_prolong = models.DateField(null = True, blank = True)
    date_rappel_1 = models.DateField(null = True, blank = True)
    date_rappel_2 = models.DateField(null = True, blank = True)
    date_rappel_3 = models.DateField(null = True, blank = True)
        
    def __unicode__(self):
        #return u" ".join(self.livre, self.perso, self.date_pret, self.date_back_prev, self.date_back_pret)
		return self.livre.titre_livre + " " + self.perso.last_name  #self.date_pret + " " + self.date_back_prev + " " + self.date_back_pret
    

# End models declaration 

