





from django.conf.urls import url
from . import views
from home.views import HomeView



urlpatterns = [

    url(r'^$', views.index),
    url(r'^chat', HomeView.as_view(), name = 'chat'),
    
    url(r'^donald/$', views.donald, name = "donald"),
    
    url(r'^gisprac_q_intro/$', views.gisprac_q_intro, name = "gisprac_q_intro"),
    url(r'^gisprac_interface/$', views.gisprac_interface, name = "gisprac_interface"),
    url(r'^gisprac_attribute/$', views.gisprac_attribute, name = "gisprac_attribute"),
    url(r'^payment2/$', views.payment2, name = "payment2"),
    
    url(r'^home/$', views.home, name = "home"),
    url(r'^index/$', views.index, name = "index"),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"),
    url(r'^item/(?P<item_id>\d+)/register/$', views.register, name = "register"),
    url(r'^item/(?P<item_id>\d+)/register/payment/$', views.payment, name = "payment"),
    #url(r'^item/(?P<item_id>\d+)/register/payment/options/$', views.options, name = "options"),
    
    url(r'^item/(?P<item_id>\d+)/payment/gisintro/$', views.gisintro, name = "gisintro"),
    url(r'^item/(?P<item_id>\d+)/payment/gistheory/$', views.gistheory, name = "gistheory"),
    url(r'^item/(?P<item_id>\d+)/payment/gispracticle/$', views.gispracticle, name = "gispracticle"),
    
    
    url(r'^item/(?P<item_id>\d+)/payment/database/$', views.database, name = "database"), 
    
    url(r'^register/$', views.register, name = "register"), 
    url(r'^connect/(?P<operation>.+)(?P<pk>\d+)/$', views.change_friends, name = "change_friends"),
  
    
    url(r'^gisintroarcgis1/$', views.gisintroarcgis1, name = "gisintroarcgis1"),
    url(r'^gisintroarcgis2/$', views.gisintroarcgis2, name = "gisintroarcgis2"),
   
 
   
    url(r'^gisintrodownload/$', views.gisintrodownload, name = "gisintrodownload"),
    
    
    url(r'^regprocess/$', views.regprocess, name = "regprocess"),
    #url(r'^gispracticle/$', views.gispracticle, name = "gispracticle"),
    
    
    url(r'^basic/$', views.basic, name = "basic"), 
    url(r'^advanced/$', views.advanced, name = "advanced"),
    url(r'^atailormade/$', views.atailormade, name = "atailormade"),
    
    
]