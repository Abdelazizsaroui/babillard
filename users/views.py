from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UpdateForm

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, f"Votre compte est créé, connectez vous avec votre nom d'utilisateur : <strong>{user.username}</strong>")
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

@login_required
def update_profile(request):
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, f"Votre profil a été mis a jour")
	return redirect('home')
	
def update_form(request):
	if request.user.is_authenticated:
		instance = request.user
		up_form = UpdateForm(instance = instance)
	else:
		up_form = UpdateForm()
	return {'up_form': up_form}