from django.shortcuts import render
from .models import Member
from AR_LAB.apps.research_publication.models import Publications

# Create your views here.
def home(request):
    context = {
            'publications' : Publication.objects.all(),
            }
    return render(request,'index.html',context)

def members(request):
    context = {
            'prof' : Member.objects.filter(designation='prof'),
            'masters' : Member.objects.filter(designation='masters'),
            'phd' : Member.objects.filter(designation='phd'),
            'des' : Member.objects.filter(designation='des'),
            'alumni' : Member.objects.filter(designation='alumni'),
            }
    return render(request,'member.html',context)

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')