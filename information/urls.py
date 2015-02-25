from django.conf.urls import patterns, url
from information import views

urlpatterns = patterns('',
	url('^$',views.speciality_list, name = "speciality_list"), 
	url(r'^(?P<speciality_id>\d+)/$', views.course_list, name='course_list'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/$', views.subject_list, name='subject_list'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/(?P<subject_id>\d+)/$', views.subject_show, name='subject_show'),
)