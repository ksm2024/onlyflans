from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hola(request):
  return HttpResponse ("Hola, onlyflans")
def hola_template(req):
    context = {
      "message": "I'm a template :)"
      }
    return render(req, 'index.html', context)
# Create your views here.
def hola_json(req):
  data = {
    "message": "Holi"
  }
  return JsonResponse(data)
