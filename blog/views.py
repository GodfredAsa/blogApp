from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Category,Author, Tags, BlogEntry, Users
from .forms import CategoryForm, TagForm, BlogEntryForm, createUserForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.shortcuts import get_404
# from django.urls import reverse

@login_required(login_url = 'blog:login')
def category_form(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()  
        form = CategoryForm()
    context = {'form': form}
    template = 'blog/category.html'
    return render(request, template, context)

# TAG FORM
@login_required(login_url = 'blog:login')
def tag_form(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TagForm()
    
    template = 'blog/tag.html'
    context = {'form': form}
    return render (request, template, context)

@login_required(login_url = 'blog:login')
def blogEntry_form(request):
    form  = BlogEntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form  = BlogEntryForm()
    template = 'blog/blog.html'
    context = {'form': form}
    return render(request, template, context)#


def register(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registration Successful ' + user )
            return redirect('blog:login')
            
            
            
    context = {'form': form}
    template = 'blog/register.html'
    return render(request, template, context)


def login_page(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username =username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('blog:category')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
            template = 'blog/login.html'
            return render(request,template)
        
    template = 'blog/login.html'
    return render(request,template)

@login_required(login_url = 'blog:login')
def logout_user(request):
    # template = 'blog/login.html'
    return redirect('blog:login')


# def index(response):
    # return HttpResponse('<h1>Hi Godfred</h1>')
# 
def index(request):
    logout(request)
    return render(request, 'index.html')
 
# def category(request):
    # category = Category.objects.all()
    # return render(request, 'category.html', {'category': category})
# 
# def tags(request):
	# tags = Tags.objects.all()
	# return render(request, 'blog/tags.html', {'tags': tags})
# 
# def author(request):
    # author = Author.objects.all()
    # return render(request, 'author.html', {'author': author})
# 
# def users(request):
    # users = Users.objects.all()
    # return render(request, 'users.html', {'users': users})
# 
# def blogEntry(request):
    # blog_entry = BlogEntry.objects.all()
    # # return render(request, 'blog_entry.html', {'blog_entry': blog_entry})