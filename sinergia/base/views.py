from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"base/home.html")

def about(request):
    return render(request,"base/about.html")
