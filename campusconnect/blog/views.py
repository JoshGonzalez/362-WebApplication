from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def chat(request):
    return render(request, 'blog/chatroom.html')

def profile(request):
    return render(request, 'blog/profile.html')
    