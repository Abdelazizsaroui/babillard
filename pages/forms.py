from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Annonce, Page

class AnnonceForm(forms.ModelForm):

	class Meta:
		model = Annonce
		fields = ['title', 'content', 'date_archive']
		widgets = {
            'content': SummernoteWidget()
        }

class PageForm(forms.ModelForm):

	class Meta:
		model = Page
		fields = ['name', 'organisme', 'private', 'login_req']
