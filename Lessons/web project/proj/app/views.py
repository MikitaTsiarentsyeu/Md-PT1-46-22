from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def posts(request):
#     post_list = ""
#     for p in Post.objects.all():
#         post_list += f"<li><h3>{p.title}</h3><p>by {p.author.name}</p></li>"

#     res = f"<h1>All posts:</h1><ul>{post_list}</ul>"

#     return HttpResponse(res)

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':all_posts})

# def post(request, id):
#     p = Post.objects.get(id=id)
#     res = f"<h3>{p.title}</h3><p>by {p.author.name}</p>"
#     return HttpResponse(res)

def post(request, id):
    p = Post.objects.get(id=id)
    return render(request, 'post.html', {'post':p})