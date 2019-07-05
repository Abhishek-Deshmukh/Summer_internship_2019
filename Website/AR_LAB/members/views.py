from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def members(request):
    context = {
            'prof' : Member.objects.filter(designation='prof'),
            'masters' : Member.objects.filter(designation='masters'),
            'phd' : Member.objects.filter(designation='phd'),
            'dese' : Member.objects.filter(designation='des'),
            'alumni' : Member.objects.filter(desgination='alumni'),
            }
    return render(request,'member.html',context)

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')
