from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# def hola(request):
#   return HttpResponse ("Hola, onlyflans")

def index (req):
  context = {
      "message": "Indice"
      # "urls": []
      # "postres": [{"name":"", "descirpcion":" " },{}]
      }
  return render(req, 'index.html', context)
  
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
