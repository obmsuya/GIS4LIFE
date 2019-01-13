from django.conf.urls import url
from . import views




urlpatterns = [

    url(r'^$', views.index),
   
     url(r'^introduction/$', views.introduction, name = "introduction"),
    url(r'^interface/$', views.interface, name = "interface"),
    
    
    #url(r'^category/(?P<id>\d+)/$', views.quiz, name = "quiz"),
    
    
    
]