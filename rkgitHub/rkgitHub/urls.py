"""rkgitHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from birds import views as birds_view
from yantrikom import views as yantrikom_view
from ldl import views as ldl_view
from home import views as home_view
from electrazz import views as electrazz_view
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header='RKGIT HUB'
admin.site.site_title='RKGIT_HUB_Admin'

urlpatterns = [
    path(r'', home_view.index),
    path('admin/', admin.site.urls),
    path(r'birds/',birds_view.index),
    path(r'ldl/',ldl_view.index),
    path(r'yantrikom/',yantrikom_view.index),
    path(r'electrazz/',electrazz_view.index),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
