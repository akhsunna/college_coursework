from django.conf.urls import patterns, url
from information import views

urlpatterns = patterns('',
	url('^$',views.speciality_list, name = "speciality_list"),
	url(r'^subject/create/$', views.create_subject, name='create_subject'),
	url(r'^labs/create/(\d+)/$', views.create_lab, name='create_lab'),
	url(r'^labs/list/(\d+)/$', views.teacher_labs_list, name='teacher_labs_list'),
	#url(r'^theory/create/(\d+)$', views.create_theory, name='create_theory'),
	url(r'^labs/edit/(\d+)/$', views.edit_labs, name='edit_labs'),
	url(r'^lecture/edit/(\d+)/$', views.edit_lecture, name='edit_lecture'),
	url(r'^subject/delete/(\d+)/$', views.delete_subject, name='delete_subject'),
	url(r'^labs/delete/(\d+)/$', views.delete_lab, name='delete_lab'),
	url(r'^lecture/delete/(\d+)/$', views.delete_lecture, name='delete_lecture'),
	url(r'^subject/edit/(\d+)/$', views.edit_subject, name='edit_subject'),
	url(r'^teacher/admin/$', views.teacher_subject_list, name='teacher_subject_list'),
	url(r'^(?P<speciality_id>\d+)/$', views.course_list, name='course_list'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/$', views.subject_list, name='subject_list'),

	url(r'^lecture/add/(\d+)/$', views.add_lecture, name='add_lecture'),
	url(r'^theory/add/(\d+)/$', views.add_theory, name='add_theory'),
	url(r'^video/add/(\d+)/$', views.add_video, name='add_video'),
	url(r'^presentation/add/(\d+)/$', views.add_presentation, name='add_presentation'),
	url(r'^test/add/(\d+)/$', views.add_test, name='add_test'),
	url(r'^test/edit/(\d+)/$', views.edit_test, name='edit_test'),
	url(r'^test/delete/(\d+)/$', views.delete_test, name='delete_test'),
)