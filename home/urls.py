





from django.conf.urls import url
from . import views
from home.views import HomeView



urlpatterns = [

    url(r'^$', views.index),
    url(r'^chat', HomeView.as_view(), name = 'chat'),
    
    url(r'^home/$', views.home, name = "home"),
    #url(r'^payment/$', views.payment, name = "payment"),
    url(r'^index/$', views.index, name = "index"),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"),
    url(r'^item/(?P<item_id>\d+)/register/$', views.register, name = "register"),
    url(r'^item/(?P<item_id>\d+)/register/payment/$', views.payment, name = "payment"),
    url(r'^item/(?P<item_id>\d+)/register/payment/options/$', views.payment_options, name = "options"),
    url(r'^item/(?P<item_id>\d+)/payment/gisintro/$', views.gisintro, name = "gisintro"),
    url(r'^gisintrostart/$', views.gisintrostart, name = "gisintrostart"),
    url(r'^gisintroarcgis1/$', views.gisintroarcgis1, name = "gisintroarcgis1"),
    url(r'^gisintroarcgis2/$', views.gisintroarcgis2, name = "gisintroarcgis2"),
    url(r'^item/(?P<item_id>\d+)/payment/database/$', views.database, name = "database"), 
    
    url(r'^register/$', views.register, name = "register"), 
    url(r'^connect/(?P<operation>.+)(?P<pk>\d+)/$', views.change_friends, name = "change_friends"),
  
      
]