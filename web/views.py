from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        "mensaje": "Indice",
        "flanes_publicos": flanes_publicos
    }
    return render(request, 'index.html', context)

      
def acerca(req):
    return render(req, 'about.html', {})

def welcome (req):
    context = {
        "message": "Bienvenidos Clientes",
        "user": "Manolo",
        "is_active": False
    }
    return render(req, 'welcome.html', context)
# Create your views here.
# def hola_json(req):
#   data = {
#     "message": "Holi"
#   }
#   return JsonResponse(data)
