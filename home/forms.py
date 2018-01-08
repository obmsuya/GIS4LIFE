from django import forms
from home.models import Post

from home.models import Post4





class HomeForm(forms.ModelForm):
    post= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'write a post....'
        }
    ))
    class Meta:
        model = Post
        fields=('post',)
        
        
        
        
class ClassRegistration(forms.ModelForm):

    class Meta:
        model = Post4
        fields = ('fullname', 'username','Proffession','subject','subtitle','phone')
