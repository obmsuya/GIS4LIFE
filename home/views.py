from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import loader


from home.forms import HomeForm, ClassRegistration, PostForm
from home.models import Post,Item, Category,Post4, Classes



    
class HomeView(TemplateView):
    template_name ='home/chat.html'
        
    def get(self, request):
        form =HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
      
        
        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)
        
    def post(self,request):
        form =HomeForm(request.POST or None)
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


#This view is for class registration- 
def create(request):
        form = ClassRegistration(request.POST or None)
        if form.is_valid():
            create = form.save(commit=False)
            create.save
            
            return redirect('home:chat')
            
        args = {'form': form}
        return render(request, 'home/create.html', args)
       
def classes_home(request):
    queryset = Classes.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "home/class_index.html", context)
    
def classes_detail(request,id):
    try:
        itm = Classes.objects.get(id=id)
    except Classes.DoesNotExist:
        itm = None
        
    context = {
        'detail': itm
    }
    return render(request, "home/class_detail.html", context)
    
def classes_create(request):
    form = PostForm(request.POST or None)
   
    if form.is_valid():
        create = form.save(commit=False)
        create.save()
            
        return redirect('home:make')
            
    args = {'form': form}
        
    return render(request, 'home/class_create.html', args)
  
#def create(request):
#        form = ClassRegistration(request.POST)
#        if form.is_valid():
#            create = form.save()
#            
#            return redirect('home:chat')
#            
#        args = {'form': form}
#        return render(request, 'home/create.html', args) 
#  