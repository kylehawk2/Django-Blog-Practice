# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from models import Blog
from django.contrib import messages

def index(request):
    return render(request, 'blog/index.html', { "blogs": Blog.objects.all() })

def update(request, id):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
       for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
       return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        return redirect('/blogs')

# def index(request):
#     response = "Index route is working!"
#     return HttpResponse(response)
