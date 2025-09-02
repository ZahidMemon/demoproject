from django.db import models

# Create your models here.

class Home(models.Model):
    title=models.CharField(max_length=100)
    info=models.TextField()

class Blog(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)

class Contact(models.Model):
    number=models.CharField(max_length=20)
    email=models.EmailField()
