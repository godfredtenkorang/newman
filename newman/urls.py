"""
URL configuration for newman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from my_site.sitemaps import *

sitemaps = {
    'static': StaticSitemap,
    'logos': LogoSitemap,
    'flyers': FlyerSitemap,
    'digital_arts': DigitalSitemap,
    'music_cover_arts': MusicSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap,{'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="my_site/robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('', include('my_site.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
