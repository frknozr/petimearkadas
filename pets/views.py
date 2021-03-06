from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Post

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from pets.forms import MyUserCreationForm, AdvertCreationForm,PetCreationForm


def index(request):
    posts = Post.objects.all()
    return render(request,"index.html",{"posts":posts})


def post_detail(request,post_id):
    return render(request,'post_detail.html',{
        'post': Post.objects.get(pk=post_id)
    })


def user_info(request,user_id):
    return render(request,'user_info.html',{
        'user': User.objects.get(pk=user_id),
    })


def register_user(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, 'register.html', {"form": form})


def add_pet(request):
    form = PetCreationForm()

    if request.method == "POST":
        form = PetCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'addpet.html', {"form":form})


def new_advert(request):
    form = AdvertCreationForm()

    if request.method == "POST":
        form = AdvertCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'advert.html', {"form": form})


def login_user(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            authenticated_user = form.get_user()
            login(request, form.get_user())
            return redirect('/', authenticated_user)

    return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('/')


