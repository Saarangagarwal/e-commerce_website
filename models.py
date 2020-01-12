from django.db import models

# Create your models here.


class Product(models.Model): #Model is a class that defines all the common characteristics and behaviour of a django application
    name = models.CharField(max_length=255) #CharField is a class in models that represents a field that can contain textual data
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer (models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

