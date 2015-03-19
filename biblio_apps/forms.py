#-*- coding: utf-8 -*-
from django.forms import ModelForm

from models import Utilisateur
from models import Auteur
from models import Proprietaire
from models import Fournisseur
from models import Editeur
from models import Livre

from models import TypeCategorie
from models import TypeSousCategorie
from models import TypeFormat
from models import TypeProprietaire
from models import TypeLangue
from models import TypeMonnaie


class UtilisateurForm(ModelForm):
    class Meta:

        model = Utilisateur
        fields = ['first_name', 'last_name', 'address', 'postcode', 'city', 'phone_prive', 'email' ]
        
        labels = {
            'last_name' : ('Nom'),
            'first_name': ('Prénom'),
            'address' : ('Addresse'), 
            'postcode' : ('Code postal'), 
            'city' : ('Localité'), 
            'phone_prive' : ('Téléphone'), 
            'email' : ('Email')
        }

class AuteurForm(ModelForm):
    class Meta:

        model = Auteur
        fields = ['nom_auteur', 'prenom_auteur']
        
        labels = {
            'nom_auteur' : ('Nom'),
            'prenom_auteur': ('Prénom'),
        }

        #help_texts = {
        #    'nom_auteur' : ('Nom de famille.'),
        #}

        error_message = { 
            'nom_auteur' : { 
                'max_length' : ("Le nom de famille est trop long."), 
            },
        }


class ProprietaireForm(ModelForm):
    class Meta:

        model = Proprietaire
        fields = ['nom_prop', 'prenom_prop', 'addr_prop', 'npa_prop', 'city_prop', 'phone_prop', 'type_prop' ]
        
        labels = {
            'nom_prop' : ('Nom'),
            'prenom_prop': ('Prénom'),
            'addr_prop' : ('Addresse'), 
            'npa_prop' : ('Code postal'), 
            'city_prop' : ('Localité'), 
            'phone_prop' : ('Téléphone'), 
            'type_prop' : ('Type prop')
        }


class FournisseurForm(ModelForm):
    class Meta:

        model = Fournisseur
        fields = ['nom_fourn', 'addr_fourn', 'npa_fourn', 'city_fourn', 'phone_fourn' ]
        
        labels = {
            'nom_fourn' : ('Nom'),
            'addr_fourn' : ('Addresse'), 
            'npa_fourn' : ('Code postal'), 
            'city_fourn' : ('Localité'), 
            'phone_fourn' : ('Téléphone'), 
        }


class EditeurForm(ModelForm):
    class Meta:

        model = Editeur
        fields = ['nom_edit', 'addr_edit', 'npa_edit', 'city_edit', 'phone_edit' ]
        
        labels = {
            'nom_edit' : ('Nom'),
            'addr_edit' : ('Addresse'), 
            'npa_edit' : ('Code postal'), 
            'city_edit' : ('Localité'), 
            'phone_edit' : ('Téléphone'), 
        }


class TypeCategorieForm(ModelForm):
    class Meta:

        model = TypeCategorie
        fields = ['nom_cate']

        labels = {
            'nom_cate' : ('Catégorie')
        }

      

class TypeSousCategorieForm(ModelForm):
    class Meta:
        model = TypeSousCategorie
        fields = ['categorie', 'nom_sous_cate']

        labels = {
            'categorie' : ('Catégorie'),
            'nom_sous_cate' : ('Sous-Catégorie')
        }


class TypeFormatForm(ModelForm):
    class Meta:

        model = TypeFormat
        fields = ['code_form', 'nom_form']

        labels = {
            'code_form' : ('Code'),
            'nom_form' : ('Format')
        }


class TypeProprietaireForm(ModelForm):
    class Meta:

        model = TypeProprietaire
        fields = ['code_prop', 'nom_prop']

        labels = {
            'code_prop' : ('Code'),
            'nom_prop' : ('Propriétaire')
        }

class TypeLangueForm(ModelForm):
    class Meta:

        model = TypeLangue
        fields = ['code_lang', 'nom_lang']

        labels = {
            'code_lang' : ('Code'),
            'nom_lang' : ('Langue')
        }

class TypeMonnaieForm(ModelForm):
    class Meta:

        model = TypeMonnaie
        fields = ['code_mone', 'nom_mone']

        labels = {
            'code_mone' : ('Code'),
            'nom_mone' : ('Monnaie')
        }


class LivreForm(ModelForm):
    #categories = ModelChoiceField(queryset=models.TypeCategorie.objects.all(), empty_label="(Nothing)")
    #souscategories = ModelChoiceField(queryset=models.TypeSousCategorie.objects.none(), empty_label=None)

    class Meta:
        model = Livre
        fields = ['titre_livre', 'nom_livre', 'form_livre', 'cate_livre', 'subcate_livre', 
                  'code_livre', 'edit_livre', 'editeur', 'annee_livre', 'class_livre', 
                  'lang_livre', 'isbn_livre', 'ean13_livre', 'monn_livre', 'prix_livre', 
                  'date_acqui', 'disp_livre', 'fournisseur', 'proprietaire', 'auteurs']

        labels = {
            'titre_livre' : ( 'Titre'), 
            'nom_livre' : ('Nom livre'),
            'form_livre' : ('Format'),
            'cate_livre' : ('Catégorie'), 
            'subcate_livre' : ('Sous-catégorie'),
            'code_livre' : ('Code'), 
            'edit_livre' : ('Edition'), 
            'editeur': ('Editeur'),
            'annee_livre' : ('Année'), 
            'class_livre' : ('Classe'), 
            'lang_livre' : ('Langue'), 
            'isbn_livre' : ('ISBN'),
            'ean13_livre' : ('EAN13'),
            'monn_livre' : ('Monnaie'), 
            'prix_livre' : ('Prix'), 
            'date_acqui' : ('Date acquision'),
            'disp_livre' : ('Disponible'),
            'fournisseur': ('Fournisseur'), 
            'proprietaire': ('Propriétaire'), 
            'auteurs' : ('Auteurs')
           
        }

       

