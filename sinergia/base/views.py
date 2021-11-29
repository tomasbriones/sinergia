from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"base/home.html")

def featured(request):
    return render(request,"base/featured.html")

def recentWork(request):
    return render(request,"base/recentWork.html")

def presentation(request):
    return render(request,"base/presentation.html")

def blogEntires(request):
    return render(request,"base/blogEntires.html")

def contactUs(request):
    return render(request,"base/contactUs.html")