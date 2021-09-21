import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import Hadits

hadits = Hadits()

def kitab(request):
  kitab = hadits.get_kitab()
  result = {
    'result': kitab
  }
  return HttpResponse(json.dumps(result, ensure_ascii=False))

def search(request, owner, kitab, id_hadits):
  data = hadits.search(owner, kitab, id_hadits)
  result = {
    'result': data
  }
  return HttpResponse(json.dumps(result, ensure_ascii=False))

def search_q(request, keyword):
  data = hadits.search_q(keyword=keyword)
  result = {
    'result': data
  }
  return HttpResponse(json.dumps(result, ensure_ascii=False))

def search_q_owner(request, owner, keyword):
  data = hadits.search_q(owner=owner, keyword=keyword)
  result = {
    'result': data
  }
  return HttpResponse(json.dumps(result, ensure_ascii=False))


def search_q_owner_kitab(request, owner, kitab, keyword):
  data = hadits.search_q(owner=owner, kitab=kitab, keyword=keyword)
  result = {
    'result': data
  }
  return HttpResponse(json.dumps(result, ensure_ascii=False))
