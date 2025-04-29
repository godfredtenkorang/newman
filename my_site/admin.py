from django.contrib import admin
from .models import Testimonial, Contact, DigitalArt, MusicCoverArt, Flyer, Logo

# Register your models here.
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(DigitalArt)
admin.site.register(MusicCoverArt)
admin.site.register(Flyer)
admin.site.register(Logo)