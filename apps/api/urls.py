from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
  path('', RedirectView.as_view(url='/')),
  path('kitab', kitab),
  path('s/<str:owner>/<str:kitab>/<int:id_hadits>', search),
  path('q/<str:keyword>', search_q),
  path('q/<str:owner>/<str:keyword>', search_q_owner),
  path('q/<str:owner>/<str:kitab>/<str:keyword>', search_q_owner_kitab),
]