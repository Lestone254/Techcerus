from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import userMsg, projectPost, clientTestimonials, blogPosts, freeQuote, userServices

# Create your views here.
def techcerus(request):
    if request.method =="POST":
        userName=request.POST.get('userName')
        telNumber=request.POST.get('telNumber')
        userEmail=request.POST.get('userEmail')
        msgHeading=request.POST.get('msgHeading')
        msgBody=request.POST.get('msgBody')
        post=userMsg()
        post.userName=userName
        post.telNumber=telNumber
        post.userEmail=userEmail
        post.msgHeading=msgHeading
        post.msgBody=msgBody
        post.save()
        redirect('techcerus')
    templatename="index.html"
    projects=projectPost.objects.all()[:4]
    testimonials=clientTestimonials.objects.all()[:4]
    blogPost = blogPosts.objects.all()[:4]
    context = {"projects":projects, "testimonials":testimonials, "blogPost":blogPost}
    return render(request, templatename, context)

def blogItem(request, pk):
    blogPost = blogPosts.objects.all()[:4]
    blog = blogPosts.objects.get(id=pk)
    templatename="blogItem.html"
    context = {"blogPost":blogPost, "blog":blog}
    return render(request, templatename, context)

def freeview(request):
    if request.method =="POST":
        userQuoteName = request.POST.get('userName')
        telQuoteNumber = request.POST.get('telQuoteNumber')
        userQuoteEmail = request.POST.get('userQuoteEmail')
        serviceQuoteCategory = request.POST.get('serviceQuoteCategory')
        msgQuoteHeading = request.POST.get('msgQuoteHeading')
        msgQuoteBody = request.POST.get('msgQuoteBody')
        post=freeQuote()
        post.userQuoteName=userQuoteName
        post.telQuoteNumber = telQuoteNumber
        post.userQuoteEmail = userQuoteEmail
        post.serviceQuoteCategory = serviceQuoteCategory
        post.msgQuoteHeading = msgQuoteHeading
        post.msgQuoteBody = msgQuoteBody
        post.save()
        return redirect('techcerus')
    templatename="freeQuote.html"
    context = {}
    return render(request, templatename, context)

def managementSystem(request):
    if request.method =="POST":
        userName=request.POST.get('userName')
        telNumber=request.POST.get('telNumber')
        userEmail=request.POST.get('userEmail')
        msgHeading=request.POST.get('msgHeading')
        msgBody=request.POST.get('msgBody')
        post=userServices()
        post.userName=userName
        post.telNumber=telNumber
        post.userEmail=userEmail
        post.msgHeading=msgHeading
        post.msgBody=msgBody
        post.save()
        redirect('techcerus')
    templatename="managementSystems.html"
    context = {}
    return render(request, templatename, context)

def mobileService(request):
    if request.method =="POST":
        userName=request.POST.get('userName')
        telNumber=request.POST.get('telNumber')
        userEmail=request.POST.get('userEmail')
        msgHeading=request.POST.get('msgHeading')
        msgBody=request.POST.get('msgBody')
        post=userServices()
        post.userName=userName
        post.telNumber=telNumber
        post.userEmail=userEmail
        post.msgHeading=msgHeading
        post.msgBody=msgBody
        post.save()
        redirect('techcerus')
    templatename="mobileServices.html"
    context = {}
    return render(request, templatename, context)

def projectItem(request, pk):
    projects = projectPost.objects.all()[:4]
    project = projectPost.objects.get(id=pk)
    templatename="projectItem.html"
    context = {'projects': projects, 'project': project}
    return render(request, templatename, context)

def uiUxDesign(request):
    if request.method =="POST":
        userName=request.POST.get('userName')
        telNumber=request.POST.get('telNumber')
        userEmail=request.POST.get('userEmail')
        msgHeading=request.POST.get('msgHeading')
        msgBody=request.POST.get('msgBody')
        post=userServices()
        post.userName=userName
        post.telNumber=telNumber
        post.userEmail=userEmail
        post.msgHeading=msgHeading
        post.msgBody=msgBody
        post.save()
        redirect('techcerus')
    templatename="uiUxDesign.html"
    context = {}
    return render(request, templatename, context)

def webDesignAndDevelopment(request):
    if request.method =="POST":
        userName=request.POST.get('userName')
        telNumber=request.POST.get('telNumber')
        userEmail=request.POST.get('userEmail')
        msgHeading=request.POST.get('msgHeading')
        msgBody=request.POST.get('msgBody')
        post=userServices()
        post.userName=userName
        post.telNumber=telNumber
        post.userEmail=userEmail
        post.msgHeading=msgHeading
        post.msgBody=msgBody
        post.save()
        redirect('techcerus')
    templatename="webDesignAndDevelopment.html"
    context = {}
    return render(request, templatename, context)