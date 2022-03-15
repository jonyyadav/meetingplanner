from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from meeting.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from meeting.models import Meeting, Room


def welcome(request):
    return render(request, "website/welcome.html",
                  {'meetings': Meeting.objects.all(), 'rooms': Room.objects.all()})
    # return HttpResponse("welcome to my website meeting planner")


def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created successfuly')
    else:
        fm = SignUpForm()
    return render(request, "signup/signup.html", {'form': fm})


def greet(request):
    return HttpResponse("hello user this site is working perfectly")


def home(request):
    return render(request, "home/home.html")


def loginUser(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                messages.success(request, 'wrong Credentials')
    else:
        fm = AuthenticationForm()
    return render(request, "login/login.html", {'form': fm})


def profile(request):
    return render(request, 'login/profile.html')


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, world'}
        return Response(content)
    
# def handle_not_found(request, exception):
#     return render(request, 'welcome.html')
    
