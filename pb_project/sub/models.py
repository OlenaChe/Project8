from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings


class Contact(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)

  def __str__(self):
    return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Contact.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.contact.save()

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  score = models.CharField(max_length=1)
  store = models.CharField(max_length=200)
  url = models.URLField()
  nutrition = models.TextField(default='X')
  img = models.TextField(default='X')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Favorite(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  favorite = models.ForeignKey(Product, default=1, related_name='substitute_product', on_delete=models.CASCADE)
  #substitute_product = models.ManyToManyField(Product, related_name='substitute_product', blank=True)
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

  def __str__(self):
    return self.contact.name




