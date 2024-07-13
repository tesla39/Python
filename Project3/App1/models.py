from django.db import models


class Student(models.Model):
    
   #created automatically as primary key by Django id= models.AutoField()
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    email = models.EmailField(null=True,blank=True)
    #address = models.TextField()
    #image = models.ImageField()
    #file= models.FileField()
    def __str__(self):
        return self.name


    
"""class Product(models.Model):
    pass """