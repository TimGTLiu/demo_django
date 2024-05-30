from django.contrib import admin
from django.urls import path
from .views import index, joke_list, add_joke, delete_joke

urlpatterns = [
    path('', index),
    path('jokes/', joke_list, name='joke_list'),
    path('jokes/add/', add_joke, name='add_joke'),
    path('jokes/delete/<int:id>/', delete_joke, name='delete_joke'),
]