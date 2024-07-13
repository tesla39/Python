from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    students=[
    {'name': 'Ram', 'class': 1},
    {'name': 'Hari', 'class': 2},
    {'name': 'Raju', 'class': 1},
    {'name': 'Gopal', 'class': 2},
    {'name': 'Shyam', 'class': 3},
    ]

    '''for student in students: #Iteration in list
        print(student)'''
    
    vegetables=[
        {'name':'potato'},
        {'name':'cabbage'},

    ]
    context= {'page': 'about'}
    return render(request,'home.html',context= {'page': 'Homepage','students':students , 'vegetables': vegetables})


def about(request):
    context= {'page': 'about'}
    return render(request,'about.html', context)