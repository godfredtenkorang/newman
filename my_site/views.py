from django.shortcuts import render, redirect
from .models import Testimonial, Contact, DigitalArt, MusicCoverArt, Flyer, Logo

# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()
    digitals = DigitalArt.objects.all()
    musics = MusicCoverArt.objects.all()
    flyers = Flyer.objects.all()
    logos = Logo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contacts = Contact(name=name, email=email, subject=subject, message=message)
        
        contacts.save()
        
        return redirect('index')
    
    context = {
        'testimonials': testimonials,
        'digitals': digitals,
        'musics': musics,
        'flyers': flyers,
        'logos': logos
    }
    return render(request, 'my_site/index.html', context)


def portfolio_detail(request):
    return render(request, 'my_site/portfolio-details.html')