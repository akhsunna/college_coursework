from django.conf.urls import patterns, url
from information import views

urlpatterns = patterns('',
	url(r'^specialities/$',views.speciality_list, name = "speciality_list"), 
	url(r'^specialities/(?P<speciality_id>\d+)/courses/$', views.course_list, name='course_list'),
	url(r'^specialities/(?P<speciality_id>\d+)/courses/(?P<course_id>\d+)/subjects', views.subject_list, name='subject_list'),
	url(r'^subjects/(?P<subject_id>\d+)/$', views.subject_show, name='subject_show'),
	url(r'^subjects/(?P<subject_id>\d+)/video/(?P<video_id>\d+)', views.video_show, name="video_show"),
	url(r'^subjects/(?P<subject_id>\d+)/theory/(?P<theory_id>\d+)', views.theory_show, name='theory_show'),
)