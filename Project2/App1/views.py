from django.shortcuts import render
from App1.models import Student
#from App1.forms import StudentForm

def home(request):
     context={}
     students=Student.objects.all()
     context['name']= students
     #context['title'] = 'home'
     return render(request, 'home.html',{'students':students})