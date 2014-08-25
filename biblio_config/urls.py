from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^biblio_apps/', include('biblio_apps.urls')),

    # Examples:
    # url(r'^$', 'biblio.views.home', name='home'),
    # url(r'^biblio/', include('biblio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
