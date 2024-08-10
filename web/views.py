from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan
from .forms import ContactForm

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        "mensaje": "Indice",
        "flanes_publicos": flanes_publicos
    }
    return render(request, 'index.html', context)

      
def acerca(request):
    return render(request, 'about.html', {})

def welcome (request):
    flanes_privados = Flan.objects.filter(is_private= True)
    return render(request, 'welcome.html', {"flanes_privados": flanes_privados})
# Create your views here.
# def hola_json(req):
#   data = {
#     "message": "Holi"
#   }
#   return JsonResponse(data)

def contacto(request):
    if request.method == 'POST':
        
        #* FORM
        form = ContactForm(request.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactForm()    
    return render(request, 'contactus.html', {'form':form})

def exito(request):
    return render(request, 'exito.html', {})

def iniciar_sesion(request):
    return render(request, 'signin.html', {})