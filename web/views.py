from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
  return HttpResponse("Hola, onlyflans")

# Create your views here.
