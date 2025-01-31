"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import  admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views.static import serve

app_name = 'accounts'
#app_name = 'home'

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include ('accounts.urls', namespace='accounts')),
    url(r'^home/', include ('home.urls', namespace='home')),
    url(r'^quiz/', include ('quiz.urls', namespace='quiz')),
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)               
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)