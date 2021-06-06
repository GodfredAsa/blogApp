from django import forms
from .models import Category, Tags, BlogEntry, Profile
 
 # IMPORTS MADE FOR ASSIGNMENT
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username','first_name', 'last_name','email', 'password1', 'password2'
        ]

# class ProfileForm(forms.ModelForm):
    # class Meta:
        # model = Profile
        # fields = ['gender'
                #   
                #   ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name',
            'category_description', 
            'category_date'
                   ]
        
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category '}),
            
            'category_description': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder': 'Enter Category Description'}),

            'category_date':forms.TextInput(attrs={'class':'form-control mt-3','type':'date'})
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ('tag',)
        
        widgets = {
            'tag': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Enter a tag', 'required': 'required'})
        }
        
class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = [
     'title', 
     'category',
     'body',
     'publication_date',
     'is_published',
     'tag'
        ]
        
    widgets = {
        'title': forms.TextInput(attrs = {'class': 'form-control mb-3', 'placeholder': 'Enter Category'}),
        
        'category': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'enter block category'}),
    
    }


        
        