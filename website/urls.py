from django.views.generic import RedirectView

from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
  path('', include('apps.home.urls')),
  path('home/', RedirectView.as_view(url='/')),
  path('api/', include('apps.api.urls')),
]