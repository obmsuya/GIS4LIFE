

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from quiz.models import *
import json
from django.http import HttpResponse

#home page



def index(request):
    template = 'quiz/index.html'
    quizs=Quiz.objects.filter(subtitle="qgis interface") 
    context = {'quizs':quizs} 
    return render (request, template, context)

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