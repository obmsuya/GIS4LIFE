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
    
    
    subject= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put subject category example Basic GIS....'
        }
    ))
    
    subtitle= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put the subtitle example Introd to GIS....'
        }
    ))
    
    username= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Put your login username....'
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
        fields = ('fullname', 'username','Proffession','subject','subtitle','phone')

#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Classes
#        fields= [
#            "title",
#            "subtitle",
#            "content",
#            "image"
#        ]