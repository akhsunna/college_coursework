from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import *
from .forms import CreateSubjectForm, PracticFileForm, PracticForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory


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
			messages.add_message(request, messages.INFO, 'Предмет успішно видалений')
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
	messages.add_message(request, messages.INFO, 'Предмет успішно видалений')
	return HttpResponseRedirect(reverse('teacher_subject_list'))

@login_required
def teacher_subject_list(request):
	subjects = Subject.objects.filter(author=request.user.id)
	return render(request, 'teacher_admin.html', {'subjects': subjects})


@login_required
def create_all(request):
	SubjectFormSet = formset_factory(CreateSubjectForm)
	if request.method == 'POST':
		subject_formset = SubjectFormSet(request.POST, request.FILES, prefix='subject')
		if subject_formset.is_valid():
			for form in subject_formset:
				name=form.cleaned_data['name']
				specialty=form.cleaned_data['specialty']
				year=form.cleaned_data['year']
				author=request.user
				new_subject = Subject(
					name=name,
					specialty=specialty,
					year=year,
					author=request.user
				)
				new_subject.save()
			messages.add_message(request, messages.INFO, 'Предмет успішно створений')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		subject_formset = SubjectFormSet(prefix='subject')
	return render(request, 'create_all.html', {
			'subject_formset': subject_formset,
			})

