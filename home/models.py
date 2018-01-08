from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
  

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Category'
        
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name




class Item(models.Model):
    class Meta:
        verbose_name_plural = 'Item'
    
    name = models.CharField(max_length= 50)
    description = models.TextField()
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.name


    
#codingEntrepreneurs vid 6    
#class Post2(models.Model):
#    title = models.CharField(max_length=120)
#    subtitle = models.CharField(max_length=120,default='')
#    content = models.TextField()
#    created_date = models.DateTimeField(
#            default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)
#    category = models.ForeignKey(category)
#
#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()
#
#    def __str__(self):
#        return self.title
    
    

    
   #This model is special for class registration 
class Post4(models.Model):
    fullname = models.CharField (max_length=100, default='')
    username = models.CharField (max_length=100, default='')
    Proffession = models.CharField (max_length=100, default='')
    subject = models.CharField (max_length=100, default='')
    subtitle = models.CharField (max_length=100, default='')
    phone = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.fullname