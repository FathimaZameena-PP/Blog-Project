from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("posts:all_posts")
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:all_posts")
    else:
        form=AuthenticationForm()
    return render(request,"users/login.html",{'form':form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("posts:all_posts")