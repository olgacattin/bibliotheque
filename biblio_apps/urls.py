from django.conf.urls import patterns, url

from biblio_apps import views

from biblio_apps.views import AuteurList, AuteurCreate, AuteurUpdate, AuteurDelete

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^livres_list/$', views.livres_list, name='livres_list'),
    url(r'^livres_detail/(?P<livre_id>\d+)/$', views.livres_detail, name='livres_detail'),
    url(r'^prets_list/$', views.prets_list, name='prets_list'),
    
    url(r'^utilisateurs_list/$', views.utilisateurs_list, name='utilisateurs_list'),
    url(r'^utilisateur_edition/$', views.utilisateur_edition, name='utilisateur_edition'),
    url(r'^utilisateur_detail/(?P<utilisateur_id>\d+)/$', views.utilisateur_detail, name='utilisateur_detail'),    
    
    url(r'^rappels_list/$', views.rappels_list, name='rappels_list'),
    
    url(r'^auteur_list/$', AuteurList.as_view(), name='auteur_list'),
    url(r'^auteur_add/$', AuteurCreate.as_view(), name='auteur_add'),
    url(r'^auteur_update/(?P<pk>\d+)/$', AuteurUpdate.as_view(), name='auteur_update'),
    url(r'^auteur_delete/(?P<pk>\d+)/$', AuteurDelete.as_view(), name='auteur_delete'),

    url(r'^fournisseurs_list/$', views.fournisseurs_list, name='fournisseurs_list'),

)
