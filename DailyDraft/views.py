from django.shortcuts import render
from .models import Draft
from django.db.models import Q


def Home(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')

def Pricing(request):
    return render(request, 'pricing.html')

def Build(request):
    return render(request, 'build.html')

def Drafts(request):    
    return render(request, 'drafts.html')

def search(request):
    query = request.GET.get('q')
    results = Draft.objects.filter(title__icontains=query)
    return render(request, "search.html", {"results": results, "query": query})