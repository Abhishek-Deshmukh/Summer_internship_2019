from django.shortcuts import render
from .models import Publication, Project

# Create your views here.
def research(request):
    context = {
            'projects' : Project.objects.all(),
    }
    return render(request,'research.html', context)

def publications(request):
    context = {
            'publications' : Publication.objects.all(),
    }
    return render(request,'publications.html', context)
