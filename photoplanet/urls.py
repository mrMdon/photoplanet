from django.conf.urls import patterns, include, url
from photoplanet.views import hello
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',(r'hello/$',hello)
    # Examples:
    # url(r'^$', 'photoplanet.views.home', name='home'),
    # url(r'^photoplanet/', include('photoplanet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
