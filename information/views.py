from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import *
from .forms import CreateSubjectForm
from django.contrib.auth.decorators import login_required


def speciality_list(request):
	specialities = Speciality.objects.all()
	return render(request,'speciality.html',{'specialities':specialities})


def course_list(request, speciality_id):
	courses = CourseNumber.objects.all()
	speciality = Speciality.objects.get(id=speciality_id)
	return render(request,'courses.html',{'courses':courses,'speciality_id':speciality_id,'speciality':speciality})


def subject_list(request, speciality_id, course_id):
	subjects = Subject.objects.filter(specialty=speciality_id,year=course_id)
	return render(request,'subjects.html',{'subjects':subjects})


def edit_subject(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	if request.method == 'POST':
		form = CreateSubjectForm(request.POST)
		if form.is_valid():
			cleand = form.cleaned_data
			subject.name = cleand['name']
			subject.specialty = cleand['specialty']
			subject.year = cleand['year']
			subject.save()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	else:
		form = CreateSubjectForm({
			'name': subject.name, 
			'specialty': subject.specialty, 
			'year': subject.year
		})
	return render(request, 'edit_subject.html', {'form': form})

def delete_subject(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	subject.delete()
	return HttpResponseRedirect('/')

@login_required
def teacher_subject_list(request, author_id):
	subjects = Subject.objects.filter(author=author_id)
	return render(request, 'teacher_admin.html', {'subjects': subjects})


@login_required
def create_subject(request):
	if request.method == 'POST':
		form = CreateSubjectForm(request.POST)
		if form.is_valid():
			cleand = form.cleaned_data
			new_subject = Subject(
					name=cleand['name'],
					specialty=cleand['specialty'],
					year=cleand['year'],
					author=request.user
				)
			new_subject.save()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	else:
		form = CreateSubjectForm()
	return render(request, 'create_subject.html', {'form': form})