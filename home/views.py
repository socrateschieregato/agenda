from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')