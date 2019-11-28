from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  score = models.CharField(max_length=1)
  store = models.CharField(max_length=200)
  url = models.URLField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Substitute(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  #usual_product = models.ForeignKey(Product, on_delete=models.CASCADE)
  substitute_product = models.ManyToManyField(Product, related_name='products', blank=True)
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE)




