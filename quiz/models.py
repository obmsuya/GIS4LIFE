from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


# Create your models here.



class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'Quiz'
    tittle = models.CharField(max_length=512, blank=True, null=True)
    subtitle = models.CharField(max_length=512, blank=True, null=True)
    question = models.CharField(max_length=512, blank=True, null=True)
    a = models.CharField(max_length=255, blank=True, null=True)
    b = models.CharField(max_length=255, blank=True, null=True)
    c = models.CharField(max_length=255, blank=True, null=True)
    d = models.CharField(max_length=255, blank=True, null=True)
    ans = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.subtitle

class TestGrades(models.Model):
    username = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=60, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    quiz_date = models.DateField(blank=True, null=True)
    #id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.username
  
  
  
class ExamGrades(models.Model):
    username = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=60, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    quiz_date = models.DateField(blank=True, null=True)
    #id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.username
   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
#class ExamResult(models.Model):
#    class Meta:
#        verbose_name_plural = 'Exam Result'
#    
#    fullname = models.CharField (max_length=250, default='')
#    username = models.CharField (max_length=250, default='')
#    course = models.CharField (max_length=250, default='')
#    phone = models.IntegerField(default=0)
#    scores = models.IntegerField(default=0)
#    
#    
#    def __str__(self):
#        return self.fullname
     
    
#class ExamReady(models.Model):
#    class Meta:
#        verbose_name_plural = 'Ready for Final Exam'
#    
#    fullname = models.CharField (max_length=250, default='')
#    username = models.CharField (max_length=250, default='')
#    course = models.CharField (max_length=250, default='')
#    date = models.CharField (max_length=250, default='')
#    time = models.CharField (max_length=250, default='')
#    phone = models.IntegerField(default=0)
#    
#    def __str__(self):
#        return self.fullname
    
