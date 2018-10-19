from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json,requests
# Create your views here.

def index(request):
    return render(request,'momo/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            return HttpResponseRedirect(reverse('login'))
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'momo/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def gh_user_search(request):
    if request.method == "POST":
        gh_username = request.POST.get('gh_username')

        #the code for search goes here!
        url1 = 'https://api.github.com/users/{user}/repos'
        url = 'https://api.github.com/users/{user}'
        response1 = requests.get(url1.format(user=gh_username))
        json_object1 = json.loads(response1.text)
        response2 = requests.get(url.format(user=gh_username))
        json_object2 = json.loads(response2.text)
        if len(json_object1) <= 2:
            user_not_exist = True
            return render(request,'momo/result.html',{'user_not_exist':user_not_exist})
        else:
            return render(request,'momo/result.html',{'json_object1':json_object1,'json_object2':json_object2,'username':gh_username})
    else:
        return render(request,'momo/search.html',{})


def gh_UserCommits(request,username,repo_name):
    url = 'https://api.github.com/repos/{user}/{repo_name}/commits'
    response = requests.get(url.format(user=username,repo_name=repo_name))
    json_object = json.loads(response.text)

    return render(request,'momo/commits_history.html',{'history':json_object,'repo_name':repo_name})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('gh_user_search')#this is where to redirect he user to search page!!!!
            else:
                return HttpResponse("USER NOT ACTIVE")
        else:
            print("someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("INVALID USERNAME or PASSWORD")
    else:
        return render(request,'momo/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("YOU ARE LOGGED IN, NICE!")
