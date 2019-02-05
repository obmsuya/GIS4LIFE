from django.conf.urls import url
from . import views
from quiz.views import exam



urlpatterns = [

    url(r'^$', views.index),
    url(r'^home/$', views.home, name = "home"),
    
     url(r'^success',views.success_, name='success'),
    url(r'^testGrade/',views.testGrade, name='testGrade'),
     url(r'^examGrade/',views.examGrade, name='examGrade'),
     
    url(r'^test/$', views.quiz, name = "test"),
    url(r'^prep/$', views.prep, name = "prep"),
    url(r'^exam/$', views.exam, name = "exam"),
     
     
    url(r'^introduction/$', views.introduction, name = "introduction"),
    url(r'^interface/$', views.interface, name = "interface"),
    
    
    
    
]