from django.conf.urls.defaults import patterns, include, url
#from django import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', 
   (r'^$', 'url.views.main'), 
   (r'^posted$', 'url.views.posted'),
   (r'^(.+)$', 'url.views.forwardurl'),
   #(r'^posted$', 'url.views.posted'),
   # (r'^(.+)$', 'url.views.forwardurl'),
    # Examples:
    #(r'^$', include('djangourl.urls')),

    # url(r'^$', 'djangourl.views.home', name='home'),
    # url(r'^djangourl/', include('djangourl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
