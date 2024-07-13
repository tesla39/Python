from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'), #path (URL address, function)
    path('about/', views.about), #name can be determined=path('about/', views.about, name='about')
    path('record/', views.FormRecord),
]