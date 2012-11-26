from django.conf.urls.defaults import patterns, include, url
from wjaa import index
from wjaa import reduzir_imagens

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',url(r'^$',index.index, name='index'),
			url(r'^reduzirImagem/$',reduzir_imagens.init, name='reduzirImagem'),
    # Examples:
    # url(r'^$', 'wjaa.views.home', name='home'),
    # url(r'^wjaa/', include('wjaa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
