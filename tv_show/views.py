from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
# Create your views here.

#Список фильмов
def movie_list(request):
    if request.method == 'GET':
        movie_list = models.Movies.objects.all().order_by('-id')
        context = {'movie_list': movie_list}
        return render(request, template_name='show.html', context=context)

def movie_detail(request, id):
    if request.method == 'GET':
        movie_id = get_object_or_404(models.Movies, id=id)
        context = {'movie_id': movie_id}
        return render(request, template_name='show_detail.html', context=context)















def greeting(request):
    if request.method == 'GET':
        return HttpResponse("Hello This is my first Project Django")

def many_emoji(request):
    if request.method == 'GET':
        return HttpResponse("😂😍😘")

def gif_image(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://i.pinimg.com/originals/9a/3c/3f/9a3c3fb5f73822af8514df07f6676392.gif'>")
