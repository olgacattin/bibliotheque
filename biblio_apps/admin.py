from django.contrib import admin
from biblio_apps.models import Auteur
from biblio_apps.models import Livre
from biblio_apps.models import Personne
from biblio_apps.models import Pret
from biblio_apps.models import Fournisseur

# Register your models here.
admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Personne)
admin.site.register(Pret)
admin.site.register(Fournisseur)


