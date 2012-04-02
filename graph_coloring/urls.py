from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#urlpatterns += staticfiles_urlpatterns()

urlpatterns = patterns('graph.views',
    (r'^$', TemplateView.as_view(template_name="graph.html")),
    url(r'^posted','posted',name='posted'),
    # Examples:
    # url(r'^$', 'graph_coloring.views.home', name='home'),
    # url(r'^graph_coloring/', include('graph_coloring.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
