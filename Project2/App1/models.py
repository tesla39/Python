from django.db import models

class Student(models.Model):
    
   #created automatically as primary key by Django id= models.AutoField()
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    
""" class Score(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField()"""

