from django.conf.urls import patterns, url

from biblio_apps import views

from biblio_apps.views import UtilisateurList, UtilisateurCreate, UtilisateurUpdate

from biblio_apps.views import AuteurList, AuteurCreate, AuteurUpdate   
from biblio_apps.views import ProprietaireList, ProprietaireCreate, ProprietaireUpdate
from biblio_apps.views import FournisseurList, FournisseurCreate, FournisseurUpdate 

from biblio_apps.views import TypeCategorieList, TypeCategorieCreate, TypeCategorieUpdate
from biblio_apps.views import TypeSousCategorieList, TypeSousCategorieCreate, TypeSousCategorieUpdate
from biblio_apps.views import TypeFormatList, TypeFormatCreate, TypeFormatUpdate
from biblio_apps.views import TypeProprietaireList, TypeProprietaireCreate, TypeProprietaireUpdate
from biblio_apps.views import TypeLangueList, TypeLangueCreate, TypeLangueUpdate
from biblio_apps.views import TypeMonnaieList, TypeMonnaieCreate, TypeMonnaieUpdate


urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^livres_list/$', views.livres_list, name='livres_list'),
    url(r'^livres_detail/(?P<livre_id>\d+)/$', views.livres_detail, name='livres_detail'),
    url(r'^prets_list/$', views.prets_list, name='prets_list'),
    
    #Table utilisateur
    url(r'^utilisateur_list/$', UtilisateurList.as_view(), name='utilisateur_list'),
    url(r'^utilisateur_add/$', UtilisateurCreate.as_view(), name='utilisateur_add'),
    url(r'^utilisateur_update/(?P<pk>\d+)/$', UtilisateurUpdate.as_view(), name='utilisateur_update'),
    url(r'^utilisateur_delete/(?P<util_id>\d+)/$', views.utilisateur_delete, name='utilisateur_delete'),

    url(r'^rappels_list/$', views.rappels_list, name='rappels_list'),

    #Table auteurs
    url(r'^auteur_list/$', AuteurList.as_view(), name='auteur_list'),
    url(r'^auteur_add/$', AuteurCreate.as_view(), name='auteur_add'),
    url(r'^auteur_update/(?P<pk>\d+)/$', AuteurUpdate.as_view(), name='auteur_update'),
    url(r'^auteur_delete/(?P<auteur_id>\d+)/$', views.auteur_delete, name='auteur_delete'),
    #url(r'^auteur_delete/(?P<pk>\d+)/$', AuteurDelete.as_view(), name='auteur_delete'),

    #Table proprietaire
    url(r'^proprietaire_list/$', ProprietaireList.as_view(), name='proprietaire_list'),
    url(r'^proprietaire_add/$', ProprietaireCreate.as_view(), name='proprietaire_add'),
    url(r'^proprietaire_update/(?P<pk>\d+)/$', ProprietaireUpdate.as_view(), name='proprietaire_update'),
    url(r'^proprietaire_delete/(?P<prop_id>\d+)/$', views.proprietaire_delete, name='proprietaire_delete'),

    #Table fournisseurs
    url(r'^fournisseurs_list/$', FournisseurList.as_view(), name='fournisseur_list'),
    url(r'^fournisseurs_add/$', FournisseurCreate.as_view(), name='fournisseur_add'),
    url(r'^fournisseurs_update/(?P<pk>\d+)/$', FournisseurUpdate.as_view(), name='fournisseur_update'),
    url(r'^fournisseurs_delete/(?P<fourn_id>\d+)/$', views.fournisseur_delete, name='fournisseur_delete'),
    
  
    #Table types - categorie
    url(r'^type_categorie_list/$', TypeCategorieList.as_view(), name='type_categorie_list'),
    url(r'^type_categorie_add/$', TypeCategorieCreate.as_view(), name='type_categorie_add'),
    url(r'^type_categorie_update/(?P<pk>\d+)/$', TypeCategorieUpdate.as_view(), name='type_categorie_update'),
    url(r'^type_categorie_delete/(?P<type_cate_id>\d+)/$', views.type_categorie_delete, name='type_categorie_delete'),

	#Table types - sous-categorie
    url(r'^type_sous_categorie_list/$', TypeSousCategorieList.as_view(), name='type_sous_categorie_list'),
    url(r'^type_sous_categorie_add/$', TypeSousCategorieCreate.as_view(), name='type_sous_categorie_add'),
    url(r'^type_sous_categorie_update/(?P<pk>\d+)/$', TypeSousCategorieUpdate.as_view(), name='type_sous_categorie_update'),
    url(r'^type_sous_categorie_delete/(?P<type_sous_cate_id>\d+)/$', views.type_sous_categorie_delete, name='type_sous_categorie_delete'),

	#Table types - format
    url(r'^type_format_list/$', TypeFormatList.as_view(), name='type_format_list'),
    url(r'^type_format_add/$', TypeFormatCreate.as_view(), name='type_format_add'),
    url(r'^type_format_update/(?P<pk>\d+)/$', TypeFormatUpdate.as_view(), name='type_format_update'),
    url(r'^type_format_delete/(?P<type_format_id>\d+)/$', views.type_format_delete, name='type_format_delete'),


	#Table types - Proprietaire
    url(r'^type_proprietaire_list/$', TypeProprietaireList.as_view(), name='type_proprietaire_list'),
    url(r'^type_proprietaire_add/$', TypeProprietaireCreate.as_view(), name='type_proprietaire_add'),
    url(r'^type_proprietaire_update/(?P<pk>\d+)/$', TypeProprietaireUpdate.as_view(), name='type_proprietaire_update'),
    url(r'^type_proprietaire_delete/(?P<type_prop_id>\d+)/$', views.type_proprietaire_delete, name='type_proprietaire_delete'),


    #Table types - Langue
    url(r'^type_langue_list/$', TypeLangueList.as_view(), name='type_langue_list'),
    url(r'^type_langue_add/$', TypeLangueCreate.as_view(), name='type_langue_add'),
    url(r'^type_langue_update/(?P<pk>\d+)/$', TypeLangueUpdate.as_view(), name='type_langue_update'),
    url(r'^type_langue_delete/(?P<type_lang_id>\d+)/$', views.type_langue_delete, name='type_langue_delete'),

    #Table types - Monnaie
    url(r'^type_monnaie_list/$', TypeMonnaieList.as_view(), name='type_monnaie_list'),
    url(r'^type_monnaie_add/$', TypeMonnaieCreate.as_view(), name='type_monnaie_add'),
    url(r'^type_monnaie_update/(?P<pk>\d+)/$', TypeMonnaieUpdate.as_view(), name='type_monnaie_update'),
    url(r'^type_monnaie_delete/(?P<type_monn_id>\d+)/$', views.type_monnaie_delete, name='type_monnaie_delete'),



)

