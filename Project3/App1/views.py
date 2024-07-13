from django.shortcuts import render   #to render HTML pages
from django.http import HttpResponse  #to handle HttpResponse
from App1.models import Student
from App1.forms import StudentForm #import form


def home(request):
    #return HttpResponse("Hello, world!")   #For HttpResponse
    return render(request, 'home.html')

def about(request):
    return HttpResponse("This is the About Page")


def FormRecord(request):
    context={}
    form =StudentForm()
    students=Student.objects.all()
    context['students']= students
    context['form']= form

    return render(request, 'FormRecord.html',context)
