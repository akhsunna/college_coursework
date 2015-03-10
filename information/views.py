from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
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



def delete_subject(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	subject.delete()
	messages.add_message(request, messages.INFO, 'Предмет успішно видалений')
	return HttpResponseRedirect(reverse('teacher_subject_list'))


def delete_lab(request, practic_id):
	practic = PracticalWork.objects.get(id=practic_id)
	practic.delete()
	messages.add_message(request, messages.INFO, 'Завдання успішно видалине')
	return HttpResponseRedirect(reverse('teacher_subject_list'))


def delete_lecture(request, lecture_id):
	lecture = Lecture.objects.get(id=lecture_id)
	lecture.delete()
	messages.add_message(request, messages.INFO, 'Лекція успішно видалина')
	return HttpResponseRedirect(reverse('teacher_subject_list'))


def delete_test(request,test_id):
	test = CheckTest.objects.get(id=test_id)
	test.delete()
	messages.add_message(request, messages.INFO, 'Підсумок успішно видалений')
	return HttpResponseRedirect(reverse('teacher_subject_list'))

@login_required
def teacher_subject_list(request):
	subjects = Subject.objects.filter(author=request.user.id)
	return render(request, 'teacher_admin.html', {
		'subjects': subjects,
		})


@login_required
def teacher_labs_list(request, subject_id):
	labs = PracticalWork.objects.filter(subject=subject_id)
	lectures = Lecture.objects.filter(subject=subject_id)
	tests = CheckTest.objects.filter(subject=subject_id)
	return render(request, 'information.html', {
		'labs': labs,
		'lectures': lectures,
		'tests':tests,
		})


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
def edit_test(request, test_id):
	test = CheckTest.objects.get(id=test_id)
	if request.method == 'POST':
		form = TestForm(request.POST, request.FILES,instance=test)
		if form.is_valid():
			cleand = form.cleaned_data
			test.title = cleand['title']
			test.doc_name = cleand['doc_name']
			test.save()
		messages.add_message(request, messages.INFO, 'Підсумок успішно змінений')
		return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		form = TestForm({
			'title': test.title, 
			'doc_name': test.doc_name, 
		}, instance=test)
	return render(request, 'edit_test.html', {'form': form})


@login_required
def add_lecture(request, subject_id):
	if request.method == 'POST':
		form = LectureForm(request.POST)
		if form.is_valid():
			cleand = form.cleaned_data
			new_lecture = Lecture(
					number=cleand['number'],
					name=cleand['name'],
					subject_id=subject_id,
				)
			new_lecture.save()
			messages.add_message(request, messages.INFO, 'Лекція успішно добавленна')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		form = LectureForm()
	return render(request, 'add_lecture.html', {'form': form})


@login_required
def add_test(request, subject_id):
	if request.method == 'POST':
		form = TestForm(request.POST, request.FILES)
		if form.is_valid():
			cleand = form.cleaned_data
			new_test = CheckTest(
					title=cleand['title'],
					doc_name=cleand['doc_name'],
					subject_id=subject_id,
				)
			new_test.save()
			messages.add_message(request, messages.INFO, 'Підумкові дані успішно добавлені')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		form = TestForm(request.POST, request.FILES)
	return render(request, 'add_test.html', {'form': form})

@login_required
def add_presentation(request, lecture_id):
	if Presentation.objects.filter(lecture_id=lecture_id).exists():
		presentation = Presentation.objects.get(lecture_id=lecture_id)
		if request.method == 'POST':
			form = PresentationForm(request.POST, request.FILES,instance=presentation)
			if form.is_valid():
				cleand = form.cleaned_data
				presentation.title = cleand['title']
				presentation.document = cleand['document']
				presentation.save()
			messages.add_message(request, messages.INFO, 'Презентація успішно змінена')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
		else:
			form = PresentationForm({
				'title': presentation.title, 
				'document': presentation.document, 
			}, instance=presentation)
		return render(request, 'edit_presentation.html', {'form': form})
	else:
		if request.method == 'POST':
			form = PresentationForm(request.POST, request.FILES)
			if form.is_valid():
				cleand = form.cleaned_data
				new_presentation = Presentation(
						title=cleand['title'],
						document=cleand['document'],
						lecture_id=lecture_id,
					)
				new_presentation.save()
				messages.add_message(request, messages.INFO, 'Презентація успішно добавленна')
				return HttpResponseRedirect(reverse('teacher_subject_list'))
		else:
			form = PresentationForm()
		return render(request, 'add_presentation.html', {'form': form})





@login_required
def add_video(request, lecture_id):
	if Video.objects.filter(lecture_id=lecture_id).exists():
		video = Video.objects.get(lecture_id=lecture_id)
		if request.method == 'POST':
			form = VideoForm(request.POST, request.FILES, instance=video)
			if form.is_valid():
				cleand = form.cleaned_data
				video.title = cleand['title']
				video.document = cleand['document']
				video.save()
			messages.add_message(request, messages.INFO, 'Відео успішно змінена')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
		else:
			form = VideoForm({
				'title': video.title, 
				'document': video.document, 
			},instance=video)
		messages.add_message(request, messages.INFO, 'Відео успішно змінене')
		return render(request, 'edit_video.html', {'form': form})
	else:
		if request.method == 'POST':
			form = VideoForm(request.POST, request.FILES)
			if form.is_valid():
				cleand = form.cleaned_data
				new_video = Video(
						title=cleand['title'],
						document=cleand['document'],
						lecture_id=lecture_id,
					)
				new_video.save()
				return HttpResponseRedirect(reverse('teacher_subject_list'))
		else:
			form = VideoForm()
		return render(request, 'add_video.html', {'form': form})


@login_required
def add_theory(request, lecture_id):
	if Theory.objects.filter(lecture_id=lecture_id).exists():
		theory = Theory.objects.get(lecture_id=lecture_id)
		if request.method == 'POST':
			form = TheoryForm(request.POST, request.FILES, instance=theory)
			if form.is_valid():
				cleand = form.cleaned_data
				theory.title = cleand['title']
				theory.document = cleand['document']
				theory.save()
				messages.add_message(request, messages.INFO, 'Теорія успішно змінена')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
		else:
			form = TheoryForm({
				'title': theory.title, 
				'document': theory.document, 
			}, instance=theory)
		return render(request, 'edit_theory.html', {'form': form})
	else:
		if request.method == 'POST':
			form = TheoryForm(request.POST, request.FILES)
			if form.is_valid():
				cleand = form.cleaned_data
				new_theory = Theory(
						title=cleand['title'],
						document=cleand['document'],
						lecture_id=lecture_id,
					)
				new_theory.save()
				messages.add_message(request, messages.INFO, 'Теорія успішно добавленна')
				return HttpResponseRedirect(reverse('teacher_subject_list'))
		else:
			form = TheoryForm(instance=theory)
		return render(request, 'add_theory.html', {'form': form})



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


@login_required
def edit_labs(request, practic_id):
	practic = PracticalWork.objects.get(id=practic_id)
	practic_file = PracticalWorkFile.objects.get(practical_work_id=practic.id)
	practic_set = formset_factory(PracticForm)
	practic_file_set = formset_factory(PracticFileForm)
	if request.method == 'POST':
		practic_formset = practic_set(request.POST, request.FILES, prefix='practic')
		practic_file_formset = practic_file_set(request.POST, request.FILES, prefix='practic_file') 
		if (practic_formset.is_valid() and practic_file_formset.is_valid()):
			for form in practic_formset:
				kind = form.cleaned_data.get('kind')
				number = form.cleaned_data.get('number')
				title = form.cleaned_data.get('title')
				practic.kind = kind 
				practic.number = number
				practic.title = title
				practic.save()
			for form in practic_file_formset:
				document = form.cleaned_data.get('document')
				practic_file.document = document
				practic_file.save()
			messages.add_message(request, messages.INFO, 'Завдання успішно змінене')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		practic_set = formset_factory(PracticForm, extra=0)
		practic_file_set = formset_factory(PracticFileForm, extra=0)
		practic_formset = practic_set(initial=[{
				'kind': practic.kind,
				'number': practic.number,
				'title': practic.title,
			}], prefix='practic')			
		practic_file_formset = practic_file_set(initial=[({
			'document': practic_file.document
			})], prefix='practic_file')
	return render(request, 'edit_labs.html', {
			'practic_formset': practic_formset,
			'practic_file_formset': practic_file_formset,
		})


@login_required
def edit_lecture(request, lecture_id):
	lecture = Lecture.objects.get(id=lecture_id)
	theory = Theory.objects.get(lecture_id=lecture.id)
	lecture_set = formset_factory(LectureForm)
	theory_set = formset_factory(TheoryForm)
	if request.method == 'POST':
		lecture_formset = lecture_set(request.POST, request.FILES, prefix='lecture')
		theory_formset = theory_set(request.POST, request.FILES, prefix='theory')
		if (lecture_formset.is_valid() and theory_formset.is_valid()):
			for form in lecture_formset:
				number = form.cleaned_data.get('number')
				name = form.cleaned_data.get('name')
				lecture.number = number
				lecture.name = name
				lecture.save()
			for form in theory_formset:
				title = form.cleaned_data.get('title')
				document = form.cleaned_data.get('document')
				theory.title = title
				theory.document = document
				theory.save()
			messages.add_message(request, messages.INFO, 'Лекція успішно змінена')
			return HttpResponseRedirect(reverse('teacher_subject_list'))
	else:
		lecture_set = formset_factory(LectureForm, extra=0)
		theory_set = formset_factory(TheoryForm, extra=0)
		lecture_formset = lecture_set(initial=[({
				'name': lecture.name,
				'number': lecture.number,
			})])
		theory_formset = theory_set(initial=[({
				'title': theory.title,
				'document': theory.document,
			})])
	return render(request, 'edit_lecture.html', {
			'lecture_formset': lecture_formset,
			'theory_formset': theory_formset,
		})

@login_required
def create_theory(request, subject_id):
	subject = Subject.objects.get(id=subject_id)
	if subject.author != request.user:
		raise PermissionDenied()
	lecture_set = formset_factory(LectureForm)
	theory_set = formset_factory(TheoryForm)
	presentation_set = formset_factory(PresentationForm)
	video_set = formset_factory(VideoForm) 
	if request.method == 'POST':
		theory_formset = theory_set(request.POST, request.FILES, prefix='theory')
		lecture_formset = lecture_set(request.POST, request.FILES, prefix='lecture')
		presentation_formset = presentation_set(request.POST, request.FILES, prefix='presentation')
		video_formset = video_set(request.POST, request.FILES, prefix='video') 
		if (lecture_formset.is_valid() and theory_formset.is_valid()
			and video_formset.is_valid() and presentation_formset.is_valid()
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


