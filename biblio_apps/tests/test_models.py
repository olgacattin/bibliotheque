# tests/test_models.py
# -*- coding: utf-8 -*-
from django.test import TestCase
from biblio_apps.models import Livre
from biblio_apps.models import Auteur
from biblio_apps.models import Pret
from biblio_apps.models import Fournisseur

from datetime import datetime

class LivreTest(TestCase):

    def test_unicode(self):
        livre = Livre.objects.create(titre_livre = "Python ", cate_livre = "PROG", code_livre = "PYTH", nom_livre = "Python2", type_livre = "PROG", edit_livre = "23443", class_livre = "Programmation", lang_livre = "FR", annee_livre = "2014", isbn_livre = "123456789098766", prix_livre = 35.80, prop_livre = "Alain Sandoz", disp_livre = True)
        self.assertEqual(livre.__unicode__(), "Python2 123456789098766 2014")


class AuteurTest(TestCase):
    
    def test_unicode(self):
        auteur = Auteur.objects.create(nom_auteur = "Gates", prenom_auteur = "Bill")
        self.assertEqual(auteur.__unicode__(), "Gates Bill") 


class PretTest(TestCase):
    
    def test_unicode(self):
        pret = Pret.objects.create(livre_id = 3 , perso_id = 1, date_pret = datetime.now() , date_back_prev = datetime.now() , date_back_pret = None)
        self.assertEqual(pret.__unicode__(), (datetime.now() datetime.now() None ))

class FournisseurTest(TestCase):
 
    def test_unicode(self):
        fourn = Fournisseur.objects.create(nom_fourn = "ABC Library", addr_fourn = "Neuchâtel", phone_fourn = "032 123 43 45")
        self.assertEqual(fourn.__unicode__(), "ABC Library Neuchâtel 032 123 43 45")

