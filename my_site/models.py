from django.db import models
from django.urls import reverse



class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials_img')
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
class DigitalArt(models.Model):
    title = models.CharField(max_length=100, default='Digital Arts')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='digital_art_img/')
    url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.name}"
    
    def get_absolute_url(self):
        return reverse('index')
    
class MusicCoverArt(models.Model):
    title = models.CharField(max_length=100, default='Music Cover Arts')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='music_cover_art_img/')
    url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.name}"
    
    def get_absolute_url(self):
        return reverse('index')
    
class Flyer(models.Model):
    title = models.CharField(max_length=100, default='Flyer')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flyer_img/')
    url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.name}"
    
    def get_absolute_url(self):
        return reverse('index')
    
class Logo(models.Model):
    title = models.CharField(max_length=100, default='Logos')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logos_img/')
    url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.name}"
    
    def get_absolute_url(self):
        return reverse('index')
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name