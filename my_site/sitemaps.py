from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Logo, Flyer, DigitalArt, MusicCoverArt

class StaticSitemap(Sitemap):
    def items(self):
        return ['index']
    
    def location(self, item):
        return reverse(item)
    
class DigitalSitemap(Sitemap):
    def items(self):
        return DigitalArt.objects.all()
    
class MusicSitemap(Sitemap):
    def items(self):
        return MusicCoverArt.objects.all()
    
class LogoSitemap(Sitemap):
    def items(self):
        return Logo.objects.all()
    
class FlyerSitemap(Sitemap):
    def items(self):
        return Flyer.objects.all()