





from django.conf.urls import url
from . import views
from home.views import HomeView



urlpatterns = [

    url(r'^$', views.list1),
    url(r'^chat', HomeView.as_view(), name = 'chat'),
    
    url(r'^home/$', views.home, name = "home"),
    url(r'^index/$', views.index, name = "index"),
    url(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"), 
     
    url(r'^list/$', views.list1, name = "list1"),
    
    #url(r'^list2/(?P<pk>\d+)/$', views.list2, name = "list2"),
    #url(r'^detail/(?P<pk>\d+)/$', views.detail, name = "detail"),
    
    
    
]