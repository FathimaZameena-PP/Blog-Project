from django.shortcuts import render
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def allPost_view(request):
    posts=Post.objects.all().order_by('-date')
    return render(request,"posts/allposts.html",{'posts':posts})

def post_detail(request,slug):
    post_page=Post.objects.get(slug=slug)
    return render(request,'posts/postPage.html',{'post':post_page})

@login_required(login_url="users:login")
def newpost(request):
    if request.method=="POST":
        form=forms.CreatePost(request.POST,request.FILES)
        if form.is_valid:
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
    else:
        form=forms.CreatePost()
    return render(request,"posts/newpost.html",{'form':form})