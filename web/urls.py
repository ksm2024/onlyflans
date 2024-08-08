
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('text/', views.hola),
    path('', views.index),
    path('about/', views.acerca),
    path('welcome/', views.welcome),
    # path('json/', views.hola_json),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

