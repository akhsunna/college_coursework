from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from .models import *

class CreateSubjectForm(ModelForm):
	class Meta:
		model = Subject
		fields = ['name', 'specialty','year']

class PracticForm(ModelForm):
	class Meta:
		model = PracticalWork
		fields = ['kind', 'number', 'title']


class PracticFileForm(ModelForm):
	class Meta:
		model = PracticalWorkFile
		fields = ['document']

class LectureForm(ModelForm):
	class Meta:
		model = Lecture
		fields = ['number', 'name']
		extra = 0

class TheoryForm(ModelForm):
	class Meta:
		model = Theory
		fields = ['title', 'document']

class PresentationForm(ModelForm):
	class Meta:
		model = Presentation
		fields = ['title', 'document']

class VideoForm(ModelForm):
	class Meta:
		model = Video
		fields = ['title', 'document']


class TestForm(ModelForm):
	class Meta:
		model = CheckTest
		fields = ['title', 'doc_name']