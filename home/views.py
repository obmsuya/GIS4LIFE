from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import loader

from home.forms import HomeForm
from home.models import Post
from .models import Item
from .models import Category
from .models import Post4
from .forms import ClassRegistration
    
class HomeView(TemplateView):
    template_name ='home/chat.html'
        
    def get(self, request):
        form =HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        print (users)
        
        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)
        
    def post(self,request):
        form =HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user =request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:chat')
            
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
        

 
def home(request):
    return render (request, "home/home.html", {})
 
 #It is written list2 but this is the first list, list of classes offered  
def index(request):
    
    context = {
       'categories':Category.objects.all() 
    }
    return render(request, 'home/index.html', context)
    
    
def item(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
        
    context = {
        'item': itm
    }
    return render(request, 'home/item.html', context)

def list1(request): 
      
    return render(request, 'home/list1.html')
  
  
    
    
    
#It is written list but this is the second list, list of subclasses   
#def list2(request, pk):
#    post = get_object_or_404(Post2, pk=pk)
#        
#    return render(request, 'home/list2.html', {'post': post})
#
##this list is special to retrive lists of subjects
# 
#def detail(request, pk):
#    post = get_object_or_404(Post2, pk=pk)
#    return render(request, 'home/detail.html', {'post': post})
#   
    
    
    
    
    
    
    
    
    
    
def register_class(request):
    if request.method == "POST":
        form = ClassRegistration(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/home', pk=post.pk)
    else:
        form = ClassRegistration()
        args = {'form': form}
    return render(request, 'home/registration.html', args)

 
