from django.conf.urls import patterns, include, url
from .views import login, logout 

urlpatterns = patterns('',
		url(r'^login/$', login, name='teacher_login'), 
		url(r'^logout/$', logout, name='teacher_logout'),
	)