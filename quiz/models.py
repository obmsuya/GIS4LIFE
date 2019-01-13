from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'Quiz'
    subtitle = models.CharField(max_length=512, blank=True, null=True)
    question = models.CharField(max_length=512, blank=True, null=True)
    a = models.CharField(max_length=255, blank=True, null=True)
    b = models.CharField(max_length=255, blank=True, null=True)
    c = models.CharField(max_length=255, blank=True, null=True)
    d = models.CharField(max_length=255, blank=True, null=True)
    ans = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.subtitle
