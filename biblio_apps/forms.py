#-*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Auteur
from models import Types

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

        error_messages = { 
            'nom_auteur' : { 
                'max_length' : ("Le nom de famille est trop long."), 
            },
        }


class CategorieForm(ModelForm):
    class Meta:

        #model = Types.objects.filter(code_table='0001')
        model = Types
        fields = ['code_type', 'nom_type']

        labels = {
            'code_type' : ('Code'),
            'nom_type' : ('Catégorie')
        }

        error_messages = {
            
        }




