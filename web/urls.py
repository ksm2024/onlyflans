
from django.urls import path 
from . import views
urlpatterns = [
    path('text/', views.hola),
    path('template/', views.hola_template),
    path('json/', views.hola_json),
    ]

