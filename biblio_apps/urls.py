from django.conf.urls import patterns, url

from biblio_apps import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^livres_list/$', views.livres_list, name='livres_list'),
    url(r'^livres_detail/(?P<livre_id>\d+)/$', views.livres_detail, name='livres_detail'),
    url(r'^prets_list/$', views.prets_list, name='prets_list'),
    url(r'^personnes_list/$', views.personnes_list, name='personnes_list'),
    url(r'^rappels_list/$', views.rappels_list, name='rappels_list'),
)
