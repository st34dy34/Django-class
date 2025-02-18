from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home_page.html")

def about(request):
    return render(request, "about_page.html")

def fake(request,id):
    return render(request, "fake.html", {"id":id})

def ukol(request,id):
    return redirect("ukol")