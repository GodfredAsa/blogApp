from django.urls import path
from . import views
app_name = 'blog'


urlpatterns = [
    # path("", views.index, name = "index"),
    # path("category/", views.category, name = "category"),
    # path("tags/", views.tags, name = "tags"),
    # path("author/", views.author, name = 'author'),
    
    # FORMS URLS ASSIGNMENT FOR WEEK FOUR
    path("categories/new/", views.category_form, name = 'category'),
    path("tagform/", views.tag_form, name = 'tag'),
    path('posts/new/', views.blogEntry_form, name = 'blog'),
    
    # LOGGED IN AND LOG OUT URL PATTERNS
    path('', views.register, name  = 'register'),
    # path('register/', views.register, name  = 'register'),
    path('login', views.login_page, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
]
    