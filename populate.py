from blog.models import  Category, Author, BlogEntry, Users

import csv
#import django
#django.setup()
import os
from django.utils import timezone
data = []

with open('populate.csv', newline = '') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = ',')
	for row in spamreader:
		data.append(row)

data = data[2:]
#print(data)

def createFields(category, author, blogEntry, users):
    cat = Category.objects.create(
    category_name = category,
    category_description = category,
    category_date = timezone.now()
    )
    cat.save()
    
    
    for author in author:
        author = Author.objects.create(
        first_name = author,
        last_name= author,
        )
    author.save()
    
    for blog in blogEntry:
        blog = BlogEntry.objects.create(
        title = blogEntry,
        body = blogEntry,
        category = blogEntry,
        publication_date = timezone.now(),
        is_published = blogEntry,
        author = blogEntry
        )
    
    blog.save()
    
    for user in users:
        user = Users.objects.create(
        username = user,
        password= user,
        confirm_password = user
        )
    user.save()
    
def populatefields(data):
    print('Script is working')
    for datapoint in data:
        category = datapoint[0:2]
        # category_name= datapoint[0:1]
        # print('Description',category_name)
        # category_description = datapoint[1:2]
        # print('\n',category)
        author = datapoint[2:4]
        # print(author)
        user = datapoint[5:6]
        print('Users :',user)
        blog  = datapoint[8:]
        
        print('end of execution', blog, '\n \n')
        
        
        createFields(category = category, author = author, blogEntry = blog, users = user)
        


    
populatefields(data)
print('Worked')
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
# 
# print(category)
# print('Author:', author)
# print('Tag:', tag)
# print('User Details:', user)
# print(blogEntry)for datapoint in data:
    # category = datapoint[0:2]
    # author = datapoint[2:4]
    # tag = datapoint[4:5]
    # user = datapoint[5:6]
    # blogEntry  = datapoint[8:]
    # 
# print(category)
# print('Author:', author)
# print('Tag:', tag)
# print('User Details:', user)
# print(blogEntry)
    # for datapoint in data:
    # category = datapoint[0:2]
    # author = datapoint[2:4]
    # tag = datapoint[4:5]
    # user = datapoint[5:6]
    # blogEntry  = datapoint[8:]
    # 
# print(category)
# print('Author:', author)
# print('Tag:', tag)
# print('User Details:', user)
# print(blogEntry)
    # for datapoint in data:
    # category = datapoint[0:2]
    # author = datapoint[2:4]
    # tag = datapoint[4:5]
    # user = datapoint[5:6]
    # blogEntry  = datapoint[8:]
    # 
# print(category)
# print('Author:', author)
# print('Tag:', tag)
# print('User Details:', user)
# print(blogEntry)
    # for datapoint in data:
    # category = datapoint[0:2]
    # author = datapoint[2:4]
    # tag = datapoint[4:5]
    # user = datapoint[5:6]
    # blogEntry  = datapoint[8:]
    # 
# print(category)
# print('Author:', author)
# print('Tag:', tag)
# print('User Details:', user)
# print(blogEntry)
    # for datapoint in data:
    # category = datapoint[0:2]
    # author = datapoint[2:4]
    # tag = datapoint[4:5]
    # user = datapoint[5:6]
    # blogEntry  = datapoint[8:]
    # 
# print(category)
# print('Author:', author)
# print('Tag:', tag)
# print('User Details:', user)
# print(blogEntry)