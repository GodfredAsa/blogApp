from django.contrib import admin
from .models import Category, Author, Tags, Users, BlogEntry, Profile


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','category_description','category_date',)

admin.site.register(Category,CategoryAdmin)

class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag',)}
    list_display = ('tag',) 
admin.site.register(Tags, TagsAdmin )

 
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('last_name',)}
    list_display = ('first_name', 'last_name',)

admin.site.register(Author, AuthorAdmin)

class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'category', 'body', 'publication_date', 'is_published', 'tag', 'author',)

admin.site.register(BlogEntry, BlogEntryAdmin)


class UsersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user_name',)}

admin.site.register(Users, UsersAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)