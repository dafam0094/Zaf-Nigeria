from django.db import models

# Create your models here.

class member(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    middel_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    how_know = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.first_name


class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    name= models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

class Publication(models.Model):
    photo = models.ImageField(upload_to='publications')
    title = models.CharField(max_length=100)
    context = models.TextField()

    def __str__(self):
        return self.title