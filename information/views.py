from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import *
from .forms import CreateSubjectForm, PracticFileForm, PracticForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory


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
			messages.add_message(request, messages.INFO, 'Предмет успішно створений')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		form = CreateSubjectForm()
	return render(request, 'create_subject.html', {'form': form})


@login_required
def create_all(request):
	SubjectFormSet = formset_factory(CreateSubjectForm)
	PracticFormSet = formset_factory(PracticForm)
	PracticFileFormSet = formset_factory(PracticFileForm)
	if request.method == 'POST':
		subject_formset = SubjectFormSet(request.POST, request.FILES, prefix='subject')
		practic_formset = PracticFormSet(request.POST, request.FILES, prefix='practic')
		practic_file_formset = PracticFileFormSet(request.POST, request.FILES, prefix='practic_file')
		if subject_formset.is_valid() and practic_file_formset.is_valid() and practic_formset.is_valid():
			cleand_subject = subject_formset.cleaned_data
			new_subject = Subject(
					name=cleand_subject['name'],
					specialty=cleand_subject['specialty'],
					year=cleand_subject['year'],
					author=request.user
				)
			new_subject.save()
			cleand_practic = practic_formset.cleaned_data
			new_practic = PracticalWork(
					kind=cleand_practic['kind'],
					title=cleand_practic['title'],
					number=cleand_practic['number'],
					subject=new_subject.id,	
				)
			new_practic.save()
			cleand_practic_file = practic_file_formset.cleaned_data
			new_practic_file = PracticalWorkFile(
					document=cleand_practic_file['document'],
					practical_work=new_practic.id,
				)
			messages.add_message(request, messages.INFO, 'Предмет успішно створений')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		subject_formset = SubjectFormSet(prefix='subject')
		practic_formset = PracticFormSet(prefix='practice')
		practic_file_formset = PracticFileFormSet(prefix='practic_file')
	return render(request, 'create_all.html', {
			'subject_formset': subject_formset,
			'practic_formset': practic_formset,
			'practic_file_formset': practic_file_formset,
			})