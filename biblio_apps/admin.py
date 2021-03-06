from django.contrib import admin
from biblio_apps.models import Auteur
from biblio_apps.models import Fournisseur
from biblio_apps.models import Livre
from biblio_apps.models import Pret
from biblio_apps.models import Proprietaire
from biblio_apps.models import TypeCategorie, TypeSousCategorie, TypeFormat, TypeProprietaire, TypeLangue, TypeMonnaie
from biblio_apps.models import Utilisateur


# Register your models here.
admin.site.register(Auteur)
admin.site.register(Fournisseur)
admin.site.register(Livre)
admin.site.register(Pret)
admin.site.register(Proprietaire)
admin.site.register(TypeCategorie)
admin.site.register(TypeSousCategorie)
admin.site.register(TypeFormat)
admin.site.register(TypeProprietaire)
admin.site.register(TypeLangue)
admin.site.register(TypeMonnaie)
admin.site.register(Utilisateur)

