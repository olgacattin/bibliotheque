#-*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Auteur

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


