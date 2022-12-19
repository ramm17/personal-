from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views={}
    views['feedbacks'] = Feedback.objects.all()
    views['contacts'] = Contact.objects.all()
    views['services'] = Service.objects.all()
    views['addresses'] = Address.objects.all()
    views['phones'] = Phone.objects.all()
    views['emails'] = Email.objects.all()
    return render(request, 'index.html', views)
    return render(request, 'contact.html', views)
def about(request):

    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):

    return render(request, 'price.html')

def services(request):

    return render(request,'services.html')

def blog_home(request):

    return render(request, 'blog-home.html')

def blog_single(request):

    return render(request, 'blog-single.html')

def elements(request):

    return render(request, 'elements.html')
