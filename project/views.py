from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def getSocial():
    return Social.objects.all()
    
def getStory():
    return Story.objects.all()

def news():
    return News.objects.all()

# Create your views here.
def home(request):
    banner, isbanner = Banner.objects.get_or_create(name='home')
    return render(request,'project/index.html', {'banner': banner, 'Social': getSocial(), 'Story': getStory(), 'News':news()})

def blog(request):
    banner, isbanner = Banner.objects.get_or_create(name='blog')
    blogs = Blog.objects.all()
    return render(request,'project/bloghome.html', {'blogs': blogs, 'banner': banner, 'Social': getSocial()})

def about(request):
    banner, isbanner = Banner.objects.get_or_create(name='about')
    context = {'banner': banner, 'Social': getSocial()}
    return render(request,'project/about.html',context)

def services(request):
    banner, isbanner = Banner.objects.get_or_create(name='services')
    context = {'banner': banner, 'Social': getSocial()}
    return render(request,'project/services.html',context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first
    context = {'blog': blog, 'Social': getSocial()}
    return render(request,'project/blogpost.html',context)

def contact(request):
    banner, isbanner = Banner.objects.get_or_create(name='contact')
    context = {'banner': banner, 'Social': getSocial()}
    return render(request,'project/contact.html',context)