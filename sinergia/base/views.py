from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """ 
    <h1>Sinergia</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
    </ul>
"""

def home(request):
    return HttpResponse(html_base + "<h2>Portada</h2>")

def about(request):
    return HttpResponse(html_base + "<h2>Acerca de</h2>")
