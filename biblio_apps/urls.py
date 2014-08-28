from django.conf.urls import patterns, url

from biblio_apps import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^livres_list/$', views.livres_list, name='livres_list'),
)
