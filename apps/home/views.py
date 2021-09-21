import re
import json

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

from apps.api.models import Hadits
import website as app 

hadits = Hadits()

def index(request):
  context = {
    'title_page': 'Home',
    'app_version': app.__version__,
    'path_hadits': hadits.get_kitab()
  }
  return render(request, 'home/index.html', context)

def search(request):
  context = {
    'title_page': 'Search',
    'app_version': app.__version__,
    'path_hadits': hadits.get_kitab()
  }
  
  get = request.GET
  id_hadits = get['id_hadits']
  if get['kitab']:
    owner = get['kitab'].split('/')[0]
    kitab = get['kitab'].split('/')[1]
    context['kitab'] = kitab
  else:
    owner = None
    kitab = None
  keyword = get['keyword']
  
  if id_hadits:
    if owner is None and kitab is None:
      messages.add_message(request, 30, 'Data Tidak Ditemukan!')
      return redirect('/')
      
    context['data'] = hadits.search(owner, kitab, id_hadits)
    context['id_hadits'] = id_hadits
  else:  
    context['data'] = hadits.search_q(owner, kitab, keyword)
    context['keyword'] = keyword
  
  if context['data'] is None:
    messages.add_message(request, 30, 'Data Tidak Ditemukan!')
    return redirect('/')
    
  return render(request, 'home/search.html', context)

def poster(request, owner, kitab, id_hadits):
  context = {
    'title_page': f'HR. {kitab.title()} : {id_hadits}',
    'app_version': app.__version__,
    'data': hadits.search(owner, kitab, id_hadits)[owner][kitab][0],
    'owner': owner,
    'kitab': kitab,
    'left': id_hadits - 1,
    'right': id_hadits + 1
  }
  
  return render(request, 'home/poster.html', context)

def about(request):
  context = {
    'title_page': 'About',
    'app_version': app.__version__,
    'repo': app.__repo__
  }
  return render(request, 'home/about.html', context)