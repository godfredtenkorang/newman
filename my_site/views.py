from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimonial, Contact, DigitalArt, MusicCoverArt, Flyer, Logo, Blog

# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()
    digitals = DigitalArt.objects.all()
    musics = MusicCoverArt.objects.all()
    flyers = Flyer.objects.all()
    logos = Logo.objects.all()
    blogs = Blog.objects.all()[:6]
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
        'logos': logos, 
        'blogs': blogs,
    }
    return render(request, 'my_site/index.html', context)

def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    
    context = {
        'blog': blog,
        'title': 'Blog'
    }
    
    return render(request, 'my_site/blog_detail.html', context)


def portfolio_detail(request):
    return render(request, 'my_site/portfolio-details.html')