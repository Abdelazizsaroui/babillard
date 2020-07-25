from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	first_name = forms.CharField(required = True, label = "Prénom")
	last_name = forms.CharField(required = True, label = "Nom")
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']