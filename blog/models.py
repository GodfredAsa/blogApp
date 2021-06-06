from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone
import datetime
# from django.template.defaultfilters import default
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class Category(models.Model):
    # category_id = models.CharField(max_length = 10, primary_key = True)
    category_name = models.CharField(max_length = 300)
    category_description = models.TextField()
    category_date = models.DateTimeField('category date')
    slug = models.SlugField(max_length=255, unique= False, null =True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name
    def get_absolute_url(self):
        return '/{}/{}/'.format('blog', self.category_name)
	
	
class Author(models.Model):
    # author_id = models.CharField(max_length = 10, primary_key = True)
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    slug = models.SlugField(max_length=255, unique=True, null =True)
    
    def __str__(self):
        return self.last_name +  ', ' + self.first_name
    
    def get_absolute_url(self):
        return '/{}/{}/'.format('blog', self.last_name)


class Tags(models.Model):
    # tag_id = models.CharField(max_length = 10, primary_key = True)
    tag = models.CharField(max_length = 300)
    slug = models.SlugField(max_length=255, unique=True, null =True)
    
    class Meta:
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return '/{}/{}/'.format('blog', self.tag)
	
	
class BlogEntry(models.Model):
    # entry_id = models.CharField(max_length = 10, primary_key = True)
    title = models.CharField(max_length = 300)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    body = models.TextField()
    publication_date = models.DateTimeField('publication date')
    is_published = models.BooleanField(default=False)
    tag = models.ForeignKey(Tags, on_delete= models.CASCADE)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, null =True)
    
    class Meta:
        verbose_name_plural = 'Blog Entries'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/{}/{}/'.format('blog', self.body)
    
	
class Users(models.Model):
    user_name = models.CharField(max_length = 300)
    password  = models.CharField(max_length = 30)
    confirm_password = models.CharField(max_length = 30)
    slug = models.SlugField(max_length=255, unique=True, null =True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.user_name
    
    def get_absolute_url(self):
        return '/{}/{}/'.format('blog', self.user_name)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    male = 'M'
    female = 'F'
    GENDER = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    gender = models.CharField(max_length = 1, choices = GENDER, blank = False, null = False)
    description = models.TextField( blank = True)
    # commented bcos pillow was not installing 
    # photo = models.ImageField(upload_to ='photos/%Y/%m/%d/',max_length = 255, null = True, blank= True)
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-gender']

    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)
    
@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

    # WRITE THE RECIEVER METHOD 8:04MIN
    
    
# class Users(AbstractUser):
    # user_name = models.CharField(max_length = 300)
    #gender = models.CharField()
    # password  = models.CharField(max_length = 30)
    # confirm_password = models.CharField(max_length = 30)
    # slug = models.SlugField(max_length=255, unique=True, null =True)
    # class Meta:
        # verbose_name = 'User'
        # verbose_name_plural = 'Users'
    # def __str__(self):
        # return self.user_name
    # def get_absolute_url(self):
        # return '/{}/{}/'.format('blog', self.user_name)