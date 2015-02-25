from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'Онлайн середовище'

urlpatterns = patterns('',
	url('^', include('information.urls')),
    url(r'grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
