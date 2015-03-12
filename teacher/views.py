from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from information.views import teacher_subject_list, speciality_list

# Create your views here.

def login(request):
	form = AuthenticationForm(request, request.POST or None)
	if request.POST:
		if form.is_valid():
			auth.login(request, form.get_user())
			return HttpResponseRedirect(reverse("teacher_subject_list"))
		else:
			return render(request, 'login.html', {'form': form})
	else:
		return render(request, 'login.html', {'form': form})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('speciality_list'))