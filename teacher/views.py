from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def login(request):
	form = AuthenticationForm(request, request.POST or None)
	if request.POST:
		if form.is_valid():
			auth.login(request, form.get_user())
			return redirect('/')
		else:
			return render(request, 'login.html', {'form': form})
	else:
		return render(request, 'login.html', {'form': form})

def logout(request):
	auth.logout(request)
	return redirect('/')