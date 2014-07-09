from django.conf.urls import patterns, include, url
from pagina.views import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^proyecto/', include('proyecto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio),
    url(r'^ingresar$', ingresar),
    url(r'^registro$', registro),
    url(r'^home/(?P<id>\d+)$',comentario),
    #gestion de usuarios
    url(r'^home$', home),
    url(r'^cerrar$', cerrar),
    url(r'^home/notas$', notas),
    url(r'^home/Todasnotas$', Todasnotas),
    url(r'^home/perfil$', perfil),
    url(r'^home/perfil/NoNotas$', NoNotas),
    url(r'^home/perfil/cambiarPass$', cambiarPass),
    url(r'^home/perfil/cambiarImagen$', cambiarImagen),
    url(r'^home/perfil/eliminar$', eliminar),

    url(r'^subir$', subirNotas),

)
