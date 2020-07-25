from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page, Annonce

class AnnonceAdmin(SummernoteModelAdmin):
	summernote_fields = ('content',)

admin.site.register(Page)
admin.site.register(Annonce, AnnonceAdmin)
    


