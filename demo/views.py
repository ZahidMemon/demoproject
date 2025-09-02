from django.shortcuts import render
from django.http import HttpResponse
from home.models import Home
from home.models import Blog
from home.models import Contact

def homePage(request):
    homePage_data=Home.objects.all()

    homePage_data_render={
        'title':homePage_data,
    }
    return render(request,'index.html',homePage_data_render)

def blogPage(request):
    blogPage_data=Blog.objects.all()

    blogPage_data_render={
        'blogData':blogPage_data,
    }
    return render(request,'blog.html',blogPage_data_render)

def contactPage(request):
    contactPage_data=Contact.objects.all()

    contactPage_data_render={
        'contactData':contactPage_data,
    }
    return render(request,'contact.html',contactPage_data_render)