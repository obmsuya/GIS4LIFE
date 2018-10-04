from django import forms
from home.models import Post
from home.models import Post4, Friend
#from home.models import Classes




class HomeForm(forms.ModelForm):
    post= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'write a post....'
        }
    ))
    
    title= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'write a title....'
        }
    ))
   

    
    class Meta:
        model = Post
        fields=('post',
                'title',
                'image'
               )
        
class MyFriend(forms.ModelForm):
    post= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'write a post....'
        }
    ))
    class Meta:
        model = Friend
        fields=('post',) 
        
        
        
        
class ClassRegistration(forms.ModelForm):
    fullname= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'First name and last name....'
        }
    ))
    
    
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put category example Basic GIS....'
        }
    ))
    
    course= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put course example Introd to GIS....'
        }
    ))
    
    username= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put your login username....'
        }
    ))
    country= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put your country....'
        }
    ))
    
    Proffession= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Example Engineering, Surveyor etc....'
        }
    ))
    

    class Meta:
        model = Post4
        fields = ('fullname', 'username','country','Proffession','category','course','phone')

#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Classes
#        fields= [
#            "title",
#            "subtitle",
#            "content",
#            "image"
#        ]