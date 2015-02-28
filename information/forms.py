from django.forms import ModelForm
from django import forms
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