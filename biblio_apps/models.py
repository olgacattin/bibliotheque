# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Model(table) : Auteur
class Auteur(models.Model):
    nom_auteur = models.CharField(max_length = 100, blank = False)
    prenom_auteur = models.CharField(max_length = 100, blank = True)
	
    def __unicode__(self):
        return self.nom_auteur + " " + self.prenom_auteur

# Model(table): Livre
class Livre(models.Model):
    LANGUE_TYPE = (
        ('FR', 'Français'),
        ('ALL', 'Allemand'),
        ('ANG', 'Anglais'),
        ('ITA', 'Italiano'),
    )
	
    LIVRE_TYPE = (
        ('MATH', 'Mathematiques'),
        ('PROG', 'Programmation'),
        ('BDON', 'Base de données'),
        ('ALGO', 'Algorithmique'),
        ('FINA', 'Finances'),
        ('MARK', 'Marketing'),
        ('DIVS', 'Divers'),
    )

    titre_livre = models.CharField(max_length = 60, blank = False)
    cate_livre = models.CharField(max_length = 5, blank = False)
    code_livre = models.CharField(max_length = 3, blank = False)
    nom_livre = models.CharField(max_length = 100, blank = False)
    type_livre = models.CharField( max_length = 4, choices = LIVRE_TYPE)
    edit_livre = models.CharField(max_length = 50, blank = True)
    class_livre = models.CharField(max_length = 10, blank = True)
    lang_livre = models.CharField(max_length = 3, choices = LANGUE_TYPE)
    annee_livre	= models.CharField(max_length = 10, blank = True)
    isbn_livre = models.CharField(max_length = 50, blank = True)
    prix_livre = models.DecimalField(max_digits = 6, decimal_places = 2)
    prop_livre = models.CharField(max_length = 100, blank = True)
    disp_livre = models.BooleanField(default = True)
    auteurs = models.ManyToManyField(Auteur)

    def __unicode__(self):
        return self.nom_livre + " " + self.isbn_livre + " " + self.annee_livre

# Model(table): Personne
class Personne(User):
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
    perso = models.ForeignKey(Personne)
    date_pret = models.DateField()
    date_back_prev = models.DateField()
    date_back_pret = models.DateField()


# Model(table): Livre/Auteur
#class LivreAuteur(models.Model):
#    id_livre = models.ForeignKey(Livre)
#    id_auteur = models.ForeignKey(Auteur)
   
    #def __unicode__(self):
    #   return self.id_livre

 
# End models declaration 

