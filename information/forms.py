from django.forms import ModelForm
from django import forms
from .models import *

class CreateSubjectForm(ModelForm):
	class Meta:
		model = Subject
		fields = ['name', 'specialty','year']