from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required


from home.forms import HomeForm, ClassRegistration
#PostForm
from home.models import Post,Item, Category,Post4,  Friend


#These class views is for chating


class HomeView(TemplateView):
    template_name ='home/chat.html'
   
    def get(self, request):
        form =HomeForm()
        posts = Post.objects.all().order_by('created')
        users = User.objects.all()
        #exclude(id=request.user.id)
    
        friend, created = Friend.objects.get_or_create(current_user=request.user)
    
        friends = friend.users.all()
  
        
        args = {'form': form, 'posts': posts, 'users': users, 'friends':friends}
        #'friends':friends
        return render(request, self.template_name, args)
        
    def post(self,request):
        form =HomeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user =request.user
            post.save()
            text = form.cleaned_data['post']
            
            
            form = HomeForm()
            return redirect('home:chat')
            
        args = {'form': form, 'text':text}
        return render(request, self.template_name, args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:chat')
 
def home(request):
    context = {
       'categories':Item.objects.all() 
    }
    return render (request, "home/home.html", context)
   
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
def register(request, item_id):
        form = ClassRegistration(request.POST or None)
        if form.is_valid():
            create = form.save()
            create.save
            
            return redirect('home:payment')
            
        args = {'form': form}
        return render(request, 'home/create.html', args)
       
def payment(request):
    return render (request, "home/payment.html")

def basic(request):    
    return render (request, "home/basic.html")
def advanced(request):    
    return render (request, "home/advanced.html")    
def atailormade(request):    
    return render (request, "home/atailormade.html")

def donald(request):    
    return render (request, "home/donald_home.html")

def gisprac_q_intro(request):    
    return render (request, "home/gisprac_q_intro.html")

def gisprac_q_datacreation(request):    
    return render (request, "home/gisprac_q_datacreation.html")

@login_required    
def gisprac_interface(request):    
    return render (request, "home/gisprac_interface.html")


    
def gisprac_attribute(request):    
    return render (request, "home/gisprac_attribute.html")

    
  
def regprocess(request):

    return render (request, "home/regprocess.html")


def gisintro(request, item_id):    
    return render (request, "home/gisintro.html")
    
@login_required    
def gistheory(request, item_id):    
    return render (request, "home/gistheory.html")    
    
def gispracticle(request, item_id):    
    return render (request, "home/gispracticle.html")    


def gisintroarcgis1(request):    
    return render (request, "home/gisintroarcgis1.html")    
def gisintroarcgis2(request):    
    return render (request, "home/gisintroarcgis2.html")
def gisintrodownload(request):    
    return render (request, "home/gisintrodownload.html")       
def database(request, item_id):    
    return render (request, "home/database.html")   
def training(request):
    return render(request, 'home/training.html')
    


