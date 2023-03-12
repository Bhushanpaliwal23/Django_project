from django.shortcuts import render,  HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        "variable1":"we are great",
        "variable2":"no i am great"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def services(request):
     return render(request,'services.html')


def contact(request):
    if request.method == "POST":
                name = request.POST.get('name')
                Email = request.POST.get('Email')
                Phone = request.POST.get('Phone')
                desc = request.POST.get('desc')
                c = Contact(name=name, Email=Email, Phone=Phone, desc=desc, date= datetime.today())
                c.save()
                messages.success(request, 'Request Sent!')
    return render(request,'contact.html')

