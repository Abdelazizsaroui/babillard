"""babillard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from pages import views as pages_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', pages_views.home, name='home'),
    path('register/', users_views.register, name='register'),
    path('page/<int:page_id>/', pages_views.page, name='page'),
    path('page/new/', pages_views.create_page, name='create-page'),
    path('annonce/<int:ann_id>/', pages_views.annonce, name='annonce'),
    path('annonce/<int:page_id>/new/', pages_views.create_annonce, name='create-annonce'),
    path('annonce/<int:ann_id>/update/', pages_views.update_annonce, name='update-annonce'),
    path('update-profile/', users_views.update_profile, name='update_profile'),
    path('search/', pages_views.search, name='search'),
    path('abonn/<int:page_id>/', pages_views.abonn, name='abonn'),
    path('add-memb/<int:page_id>/', pages_views.add_memb, name='add-memb')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)