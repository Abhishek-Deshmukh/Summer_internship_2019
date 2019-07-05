from django.shortcuts import render
from .models import Publications

# Create your views here.
def research(request):
    return render(request,'research.html')

def publications(request):
    context = {
            'publications' : Publications.objects.all(),
    }
    return render(request,'publications.html', context)
