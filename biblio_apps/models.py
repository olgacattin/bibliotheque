# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime 

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Model(table): Types
class Types(models.Model):
    code_table = models.CharField(max_length = 5, null = False, blank = False)
    nom_table = models.CharField(max_length = 30, null = True, blank = True)
    code_type = models.CharField(max_length = 5, null = False, blank = False)
    nom_type = models.CharField(max_length = 30, null = True, blank = True)
    code_pere = models.CharField(max_length = 5, null = True, blank = True)

    def __unicode__(self):
        return self.code_table + " " + self.nom_table + " " + self.code_type + " " + self.nom_type + " " + self.code_pere


# Model(table): Auteur
class Auteur(models.Model):
    nom_auteur = models.CharField(max_length = 100, blank = False)
    prenom_auteur = models.CharField(max_length = 100, blank = True)
	
    def __str__(self):
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
        return self.nom_fourn + " " + self.addr_fourn + " " + self.phone_fourn


# Model(table): Proprietaire
class Proprietaire(models.Model):
    nom_prop = models.CharField(max_length = 150, blank = False)
    prenom_prop = models.CharField(max_length = 150, blank = False)
    addr_prop = models.CharField(max_length = 150, blank = True)
    npa_prop = models.CharField(max_length = 4)
    city_prop = models.CharField(max_length = 50)
    phone_prop = models.CharField(max_length = 50, blank = True)
    type_prop = models.ForeignKey(Types, related_name = 'proprietaire')

    def __unicode__(self):
       return self.nom_prop + " " + self.prenom_prop + " " + self.phone_prop


# Model(table): Livre
class Livre(models.Model):

    titre_livre = models.CharField(max_length = 60, blank = False)
    cate_livre = models.ForeignKey(Types, related_name = 'categorie')
    code_livre = models.CharField(max_length = 3, blank = False)
    nom_livre = models.CharField(max_length = 100, blank = False)
    type_livre = models.ForeignKey(Types, related_name = 'type_livre')
    subtype_livre = models.ForeignKey(Types, null=True, blank=True, related_name = 'sub_type_livre')
    edit_livre = models.CharField(max_length = 50, blank = True)
    class_livre = models.CharField(max_length = 10, blank = True)
    lang_livre = models.ForeignKey(Types, related_name = 'langue')
    annee_livre	= models.CharField(max_length = 10, blank = True)
    isbn_livre = models.CharField(max_length = 50, blank = True)
    prix_livre = models.DecimalField(max_digits = 6, decimal_places = 2)
    monn_livre = models.ForeignKey(Types, null=True, blank=True, related_name = 'type_monnaie')
    disp_livre = models.BooleanField(default = True)
    date_acqui = models.DateField(default = datetime.now(), null = True, blank = True)
    fournisseur = models.ForeignKey(Fournisseur)
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

