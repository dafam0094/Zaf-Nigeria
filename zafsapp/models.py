from django.db import models

# Create your models here.

class member(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    contact_address = models.CharField(max_length=200, null=True)
    residential_address = models.CharField(max_length=200, null=True)
    how_know = models.CharField(max_length=200, null=True)
    upload_photo = models.ImageField(upload_to='photos/')
    

    def __str__(self):
        return self.full_name


class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    name= models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

class Publication(models.Model):
    photo = models.ImageField(upload_to='publications')
    title = models.CharField(max_length=300)
    context = models.TextField()

    def __str__(self):
        return self.title

class Donation(models.Model):
    name = models.CharField(max_length=255)
    Email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)