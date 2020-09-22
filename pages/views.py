import string
import random
import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Annonce, Page
from .forms import AnnonceForm, PageForm
from users.forms import UpdateForm

def home(request):
	user = request.user
	if user.is_authenticated:
		pages = user.abonn.all()
		annonces = Annonce.objects.filter(page__in=pages, archive=False)
		return render(request, 'home.html', {'annonces': annonces})
	return render(request, 'home.html')

@login_required
def create_page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			page.user = request.user
			code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
			page.code = code
			page.save()
			if page.private:
				page.members.add(request.user)
			messages.success(request, f"Votre page <strong>{page.name}</strong> est créée, son code est <strong>{page.code}</strong>")
			return redirect(reverse('page', kwargs={'page_id': page.id}))
	else:
		form = PageForm()
	return render(request, 'create_page.html', {'form': form})

@login_required
def create_annonce(request, page_id):
	page = Page.objects.get(id=page_id)
	if request.method == 'POST':
		form = AnnonceForm(request.POST)
		if form.is_valid():
			ann = form.save(commit=False)
			ann.page = page 
			ann.save()
			messages.success(request, f"Vous avez publié une annonce sur la page <strong>{page.name}</strong>")
			return redirect(reverse('annonce', kwargs={'ann_id': ann.id}))
	else:
		form = AnnonceForm()
	return render(request, 'create_annonce.html', {'form': form, 'page': page})

@login_required
def update_annonce(request, ann_id):
	ann = Annonce.objects.get(id=ann_id)
	if ann.page.user != request.user:
		raise PermissionDenied
	if request.method == 'POST':
		form = AnnonceForm(request.POST)
		if form.is_valid():
			title = request.POST.get('title')
			ann.title = title
			content = request.POST.get('content')
			ann.content = content
			date_archive = request.POST.get('date_archive')
			ann.date_archive = date_archive
			ann.save()
			messages.success(request, f"Vous avez modifier l'annonce <strong>{ann.title}</strong>")
			return redirect(reverse('annonce', kwargs={'ann_id': ann_id}))
	else:
		form = AnnonceForm(instance=ann)
	return render(request, 'update_annonce.html', {'form': form, 'ann': ann})

def delete_annonce(request, ann_id):
	ann = Annonce.objects.get(id=ann_id)
	if ann.page.user != request.user:
		raise PermissionDenied
	else:
		ann.delete()
	return redirect(reverse('page', kwargs={'page_id': ann.page.id}))

def page(request, page_id):
	page = Page.objects.get(id=page_id)
	if page.login_req and not request.user.is_authenticated:
		return redirect('login')
	if page.private and request.user not in page.members.all():
		raise PermissionDenied
	if page.user == request.user:
		template = "page_back.html"
	else:
		template = "page_front.html"
	return render(request, template, {'page': page})

def annonce(request, ann_id):
	annonce = Annonce.objects.get(id=ann_id)
	return render(request, 'annonce.html', {'annonce': annonce})

def search(request):
	q = request.GET.get("search")
	if q:
		try:
			page = Page.objects.get(code=q)
			return redirect(reverse('page', kwargs={'page_id': page.id}))
		except:
			messages.warning(request, '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-frown"><circle cx="12" cy="12" r="10"></circle><path d="M16 16s-1.5-2-4-2-4 2-4 2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg> Aucune page trouvée avec le code entré. Veuillez vérifier le code et réessayer!')
			return redirect(request.META['HTTP_REFERER'])

@login_required
def abonn(request, page_id):
	page = Page.objects.get(id=page_id)
	if request.user in page.abonn.all():
		page.abonn.remove(request.user)
	else:
		page.abonn.add(request.user)
	return redirect(request.META['HTTP_REFERER'])

def add_memb(request, page_id):
	page = Page.objects.get(id=page_id)
	if request.user != page.user:
		raise PermissionDenied
	if request.method == 'POST':
		if request.POST.get('mmb_list'):
			mmb_list = request.POST.get('mmb_list')
			lst = mmb_list.split(",")
			cleaned_lst = [el.strip() for el in lst]
			for email in cleaned_lst:
				try:
					users = User.objects.filter(email=email)
					for user in users:
						page.members.add(user)
				except:
					# Ajouter ici la logique pour ajouter user
					# quand il crée un compte
					pass
	return redirect(request.META['HTTP_REFERER'])

def archive(request, ann_id):
	ann = Annonce.objects.get(id=ann_id)
	action = "activée" if ann.archive else "archivée"
	ann.archive = False if ann.archive else True
	ann.save()
	messages.success(request, f"L'annonce <strong>{ann.title}</strong> a été {action}!")
	return redirect(request.META['HTTP_REFERER'])

