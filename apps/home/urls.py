from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('search', search),
    path('about', about),
    path('poster/<str:owner>/<str:kitab>/<int:id_hadits>', poster),
]
