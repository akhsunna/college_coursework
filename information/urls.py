from django.conf.urls import patterns, url
from information import views

urlpatterns = patterns('',
	url('^$',views.speciality_list, name = "speciality_list"), 
	url(r'^(?P<speciality_id>\d+)/$', views.course_list, name='course_list'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/$', views.subject_list, name='subject_list'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/(?P<subject_id>\d+)/$', views.subject_show, name='subject_show'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/(?P<subject_id>\d+)/video/(?P<video_id>\d+)/$', views.video_show, name="video_show"),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/(?P<subject_id>\d+)/theory/(?P<theory_id>\d+)/$', views.theory_show, name='theory_show'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/(?P<subject_id>\d+)/pr/(?P<pr_id>\d+)/$', views.pr_show, name='pr_show'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/(?P<subject_id>\d+)/lr/(?P<pr_id>\d+)/$', views.pr_show, name='pr_show'),
)