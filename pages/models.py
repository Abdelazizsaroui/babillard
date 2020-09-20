from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
	name = models.CharField(max_length=150, verbose_name='Nom de la page')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	organisme = models.CharField(max_length=150, verbose_name="Nom de l'organisme (facultatif)", blank=True)
	code = models.CharField(max_length=10, default='0000000000')
	private = models.BooleanField(default=False, verbose_name="Page privé", help_text="Seuls les utilisateurs autorisés peuvent visiter la page et voir ses annonces")
	members = models.ManyToManyField(User, related_name='members', blank=True)
	abonn = models.ManyToManyField(User, related_name='abonn', blank=True)
	login_req = models.BooleanField(default=False, verbose_name="Authentification requise", help_text="Cochez cette case si les utilisateurs annonymes ne sont pas autorisés à visiter la page et voir ses annonces")

	def __str__(self):
		return self.name

class Annonce(models.Model):
	title = models.CharField(max_length=255, verbose_name="Titre de l'annonce")
	content = models.TextField(verbose_name="Contenu")
	page = models.ForeignKey(Page, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add=True)
	date_archive = models.DateTimeField(blank = True , null = True , verbose_name = "Date d'archivage (facultative)")
	archive = models.BooleanField(default = False)

	def __str__(self):
		return self.title

