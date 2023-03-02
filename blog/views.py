from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blog.html',{'blogs':blogs})

def detais(request, id_blog):
    blog = get_object_or_404(Blog, pk = id_blog)
    return render(request, 'blog/detais.html',{'blog':blog})
# def home(request):
#     projects = Project.objects.all()
#     return render(request,'portfolio/home.html',{'projects':projects})
