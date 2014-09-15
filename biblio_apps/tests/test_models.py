# tests/test_models.py
from django.test import TestCase
from biblio_apps.models import Livre
from biblio_apps.models import Auteur

class LivreTest(TestCase):

    def test_unicode(self):
        livre = Livre.objects.create(titre_livre = "Python ", cate_livre = "PROG", code_livre = "PYTH", nom_livre = "Python2", type_livre = "PROG", edit_livre = "23443", class_livre = "Programmation", lang_livre = "FR", annee_livre = "2014", isbn_livre = "123456789098766", prix_livre = 35.80, prop_livre = "Alain Sandoz", disp_livre = True)
        self.assertEqual(livre.__unicode__(), "Python2 123456789098766 2014")


class AuteurTest(TestCase):
    
    def test_unicode(self):
        auteur = Auteur.objects.create(nom_auteur = "Gates", prenom_auteur = "Bill")
        self.assertEqual(auteur.__unicode__(), "Gates Bill") 


#class PretTest(TestCase):
#    def test_unicode(self):
#        pret = Pret.objects.create(livre =  , perso = "Olga Cattin", date_pret = , date_back_prev = , date_back_pret = )
    

