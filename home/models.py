from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField (max_length=120, default = "")
    theory = models.CharField(max_length=200)
    practicle = models.CharField (max_length=120, default = "")
    exam = models.CharField (max_length=120, default = "")
    results = models.CharField (max_length=120, default = "")
    image = models.ImageField(null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
  
class Friend(models.Model):
    users = models.ManyToManyField(User)
    post = models.CharField(max_length=200, default= "")
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.PROTECT)
    
    
    
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)
    
    
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)



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
    subtitle = models.CharField (max_length=120, default='Introduction to GIS')
    description = models.TextField()
    link = models.TextField(default = "")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    

     
#This model is for class registration 
class Post4(models.Model):
    class Meta:
        verbose_name_plural = 'Students Request'
    
    fullname = models.CharField (max_length=100, default='')
    username = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    Proffession = models.CharField (max_length=100, default='')
    category = models.CharField (max_length=100, default='')
    course = models.CharField (max_length=100, default='')
    phone = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.fullname
    

   
    