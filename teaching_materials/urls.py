from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
	url('^', include('information.urls')),
    url(r'grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 

if settings.DEBUG:
	urlpatterns += patterns('',
 	   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
