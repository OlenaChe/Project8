from django.db import models

class Contact(models.Model):
  email = models.EmailField(max_length=100)
  name = models.CharField(max_length=100)
  
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
  data = models.DataTimeField(auto_now_add = True)
  favorite_list = models.BooleanField(default = False)
  usual_product = models.ForeignKey(Product)
  substitute_product = models.ForeignKey(Product)
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE)





