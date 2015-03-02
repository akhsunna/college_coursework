from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import *
from .forms import *
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
			messages.add_message(request, messages.INFO, 'Предмет успішно змінений')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
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
			messages.add_message(request, messages.INFO, 'Предмет успішно добавлений')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		form = CreateSubjectForm()
	return render(request, 'create_subject.html', {'form': form})


@login_required
def create_lab(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	practic_set = formset_factory(PracticForm)
	file_set = formset_factory(PracticFileForm)
	if request.method == 'POST':
		practic_formset = practic_set(request.POST, request.FILES, prefix='practic')
		file_formset = file_set(request.POST, request.FILES, prefix='practic_file')
		if (practic_formset.is_valid() and file_formset.is_valid() ):
			for form in practic_formset:
				kind = form.cleaned_data.get('kind')
				number = form.cleaned_data.get('number')
				title = form.cleaned_data.get('title')
				new_practic = PracticalWork(
						kind=kind,
						number=number,
						title=title,
						subject_id=subject.id,
					)
				new_practic.save()
			for form in file_formset:
				document = form.cleaned_data.get('document')
				new_file = PracticalWorkFile(
						document=document,
						practical_work_id=new_practic.id
					)
				new_file.save()
			messages.add_message(request, messages.INFO, 'Робота успішно добавленна')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		practic_formset = practic_set(prefix='practic')
		file_formset = file_set(prefix='practic_file')
	return render(request, 'create_lab.html', {
		'practic_formset': practic_formset,
		'file_formset': file_formset,
		})


@login_required
def create_theory(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	lecture_set = formset_factory(LectureForm)
	theory_set = formset_factory(TheoryForm)
	presentation_set = formset_factory(PresentationForm)
	video_set = formset_factory(VideoForm) 
	if request.method == 'POST':
		theory_formset = theory_set(request.POST, request.FILES, prefix='theory')
		lecture_formset = lecture_set(request.POST, request.FILES, prefix='lecture')
		presentation_formset = presentation_set(request.POST, request.FILES, prefix='presentation')
		video_formset = video_set(request.POST, request.FILES, prefix='video') 
		if ( 	theory_formset.is_valid()
				and lecture_formset.is_valid()  
				and presentation_formset.is_valid()
				and video_formset.is_valid()
			):
			for form in lecture_formset:
				number = form.cleaned_data.get('number')
				name = form.cleaned_data.get('name')
				new_lecture = Lecture(
						number=number,
						name=name,
						subject_id=subject.id
					)
				new_lecture.save()
			for form in theory_formset:
				title = form.cleaned_data.get('title')
				document = form.cleaned_data.get('document')
				new_theory = Theory(
						title=title,
						document=document,
						lecture_id=new_lecture.id
					)
				new_theory.save()
			for form in video_formset:
				title = form.cleaned_data.get('title')
				document = form.cleaned_data.get('document')
				new_video = Video(
						title=title,
						document=document,
						lecture_id=new_lecture.id
					)
				if new_video.title!=None:
					new_video.save()
			for form in presentation_formset:
				title = form.cleaned_data.get('title')
				document = form.cleaned_data.get('document')
				new_presentation = Presentation(
						title=title,
						document=document,
						lecture_id=new_lecture.id
					)
				if new_presentation.title!=None:
					new_presentation.save()
			messages.add_message(request, messages.INFO, 'Теоретичний матеріал успішно доданий')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		lecture_formset = lecture_set(prefix='lecture')
		theory_formset = theory_set(prefix='theory')
		presentation_formset = presentation_set(prefix='presentation')
		video_formset = video_set(prefix='video')
	return render(request, 'create_theory.html', {
			'lecture_formset': lecture_formset,
			'theory_formset': theory_formset,
			'presentation_formset': presentation_formset,
			'video_formset': video_formset,
		})



