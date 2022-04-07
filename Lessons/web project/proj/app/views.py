from datetime import datetime
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Author, Post
from .forms import AddPost, AddPostModelForm

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
    print(request.user.email)
    return render(request, 'posts.html', {'posts':all_posts})

# def post(request, id):
#     p = Post.objects.get(id=id)
#     res = f"<h3>{p.title}</h3><p>by {p.author.name}</p>"
#     return HttpResponse(res)

def post(request, id):
    p = Post.objects.get(id=id)
    return render(request, 'post.html', {'post':p})



def add_post(request):

    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post = Post()
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()
            post.title = form.cleaned_data['title']
            post.subtitle = form.cleaned_data['subtitle']
            post.content = form.cleaned_data['content']
            post.post_type = form.cleaned_data['post_type']
            post.image = form.cleaned_data['image']

            post.save()

            return redirect('posts')
    else:
        form = AddPost()

    return render(request, 'add_post.html', {'form':form})

def add_post_model_form(request):

    if request.method == 'POST':
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()
            post.save()
            form.save_m2m()
            # post = Post()
            # post.author = Author.objects.all()[0]
            # post.issued = datetime.now()
            # post.title = form.cleaned_data['title']
            # post.subtitle = form.cleaned_data['subtitle']
            # post.content = form.cleaned_data['content']
            # post.post_type = form.cleaned_data['post_type']
            # post.image = form.cleaned_data['image']

            # post.save()

            return redirect('posts')
    else:
        form = AddPostModelForm()

    return render(request, 'add_post.html', {'form':form})