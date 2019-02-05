

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect,reverse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
#from accounts.view import logout
from quiz.models import *
import json
import random
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from datetime import datetime

#from quiz.forms import SignUpForm,Login_Form
from django.contrib.auth import login , authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm













#home page


def home(request):
    template = 'quiz/exam_home.html'
    return render (request, template)
    
def index(request):
    template = 'quiz/index.html'
    quizs=Quiz.objects.filter(subtitle="qgis interface") 
    context = {'quizs':quizs} 
    return render (request, template, context)

def prep(request):
    template = 'quiz/prep.html'
    
    pool= list( Quiz.objects.all() )
    random.shuffle( pool )
    quizs = pool[:2]
    
    context = {'quizs':quizs} 
    return render (request, template, context)
    
def quiz(request):
    template = 'quiz/quiz.html'
    quizs=Quiz.objects.filter(subtitle="qgis interface") 
    context = {'quizs':quizs} 
    return render (request, template, context)
    

def exam(request):
    template = 'quiz/exam_intro_q_gis.html'
    
    pool= list( Quiz.objects.all() )
    random.shuffle( pool )
    quizs = pool[:2]
    
    context = {'quizs':quizs} 
    return render (request, template, context)
    

    
def success_(request):
    template = 'quiz/success.html'
    # Kill sesion
    Session.objects.all().delete() 
    c= Quiz.objects.count() 
    if 'grade' in request.GET:
        grade=int(request.GET['grade'])
    else:
        grade = 0
    context = {
      'grade':grade, 'c':c, 'r':str(grade)+'/'+str(c)
           
    }
    
    return render (request, template, context)
    

#def success2_(request):
#    template = 'quiz/success2.html'
#    # Kill sesion
#    Session.objects.all().delete() 
#    c= Quiz.objects.count() 
#    if 'grade' in request.GET:
#        grade=int(request.GET['grade'])
#    else:
#        grade = 0
#    context = {
#      'grade':grade, 'c':c, 'r':str(grade)+'/'+str(c)
#           
#    }
#    
#    return render (request, template, context)
    
def testGrade(request):
    
    grade = request.GET['grade']
   
    if request.user.is_authenticated:
        
        #save to db
        obj= TestGrades(grade = grade,username=request.user.username,firstname  = request.user.first_name,
            email  = request.user.email, quiz_date=datetime.now() ,id=TestGrades.objects.count()+1 )
        obj.save()
        #save_db_field(username,grade,firstname,email)

        return render(request, 'quiz/success.html', {'grade': grade})
    else:
        pass



def examGrade(request):
    
    grade = request.GET['grade']
   
    if request.user.is_authenticated:
        
        #save to db
        obj= ExamGrades(grade = grade,username=request.user.username,firstname  = request.user.first_name,
            email  = request.user.email, quiz_date=datetime.now() ,id=ExamGrades.objects.count()+1 )
        obj.save()
        #save_db_field(username,grade,firstname,email)

        return render(request, 'quiz/success.html', {'grade': grade})
    else:
        pass






























def introduction(request):
    template = 'quiz/test_q_intro.html'
    quizs=Quiz.objects.filter(subtitle="qgis introduction") 
    context = {'quizs':quizs} 
    return render (request, template, context)

def interface(request):
    template = 'quiz/test_interface.html'
    quizs=Quiz.objects.filter(subtitle="qgis interface") 
    context = {'quizs':quizs} 
    return render (request, template, context)
    



        
        
    
   
    

    
        
        
