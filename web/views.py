from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# def hola(request):
#   return HttpResponse ("Hola, onlyflans")

def index(req):
    context = {
        "message": "Indice",
        "postres": [
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-2.jpg?size=768x509&lossy=2&strip=1&webp=1",
                "name": "Tarta de chocolate",
                "description": "Una delicia que lleva dos planchas de bizcocho de chocolate, separadas por una fina capa de mermelada de damasco y recubiertas con un glaseado de chocolate."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-3.jpg?size=768x509&lossy=2&strip=1&webp=1",
                "name": "Tiramisú", 
                "description": "Bizcocho humedecido con una mezcla de café y licor y superponerlo en capas, alternando entre la crema y el bizcocho."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-4.jpg?size=768x512&lossy=2&strip=1&webp=1",
                "name": "Panna Cotta", 
                "description": "Parecido al flan y con una textura suave y gelatinosa."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-6.jpg?size=768x511&lossy=2&strip=1&webp=1",
                "name": "Pávlola", 
                "description": "Consiste en una base de merengue horneado sobre la cual se coloca crema batida, chocolate y trozos de fruta, en especial los frutos rojos."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-8.jpg?size=768x448&lossy=2&strip=1&webp=1",
                "name": "Crema de papaya", 
                "description": "Este postre está hecho a base de una crema de papaya y se acostumbra servirlo con helado de vainilla."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-011.jpg?size=768x477&lossy=2&strip=1&webp=1",
                "name": "Milhojas", 
                "description": "Este crujiente postre está hecho de finas capas de masa hojaldre y lleva crema pastelera o crema de leche, tal vez ambos si eres fan del dulce y por encima está cubierto con azúcar impalpable."
            }
        ]  
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
