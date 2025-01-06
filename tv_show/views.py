from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting(request):
    if request.method == 'GET':
        return HttpResponse("Hello This is my first Project Django")

def many_emoji(request):
    if request.method == 'GET':
        return HttpResponse("😂😍😘")

def gif_image(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://i.pinimg.com/originals/9a/3c/3f/9a3c3fb5f73822af8514df07f6676392.gif'>")
