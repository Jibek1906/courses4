from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting, name='greeting'), # views.greeting - название функции в views.py
    path('emoji/', views.many_emoji, name='emoji'),
    path('image/', views.gif_image, name='image'),
]