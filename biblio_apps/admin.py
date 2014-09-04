from django.contrib import admin
from biblio_apps.models import Auteur
from biblio_apps.models import Livre
from biblio_apps.models import Personne
from biblio_apps.models import Pret

# Register your models here.
admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Personne)
admin.site.register(Pret)


