from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + username)
                return redirect('main-home')
    
        context = {
            'form' : form,
        }
        return render(request, 'members/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, "members/login.html")

def logout_user(request):
    logout(request)
    return redirect('user-login')


def profile(request):
    return render(request, "members/profile.html")

def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() 
            profile_form.save()
            return redirect("user-profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context= {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request, 'members/profile_update.html',context)