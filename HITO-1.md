pip3.2.# HITO 1 - PROYECTO
1. Levantar primer proyecto en Django
  - Utiliza el administrador de paquetes PIP para la instalación de los componentes Django.
  1. Crea la carpeta onlyflans 
  2. Dentro de esta crea un entorno virtual
  python -m venv venv
  3. Activar 
  source venv/Scripts/activate
  4. Instala Django 
  pip install django==5.0.7 --trusted-host pypi.org --trusted-host files.pythonhosted.org
    pip freeze
  5. Crea un project con el llamado onlyflans (recuerden usar el punto al final) -->
  django-admin startproject onlyflans .
  6. Probar el Proyecto ejecutando runserver
  python manage.py runserver
  7. Preparar y migrar
  python manage.py makemigrations
  python manage.py migrate
  8. Crear user y password del admin
  python manage.py createsuperuser
  9. Probar el Proyecto ejecutando runserver e ingresar como admin
  /admin
  10. Crear una app llamada web
  python manage.py startapp web

  11. Armar la estructura
    - static
        - js index.js console.log(" ")
        - css index.css
        -favicon
        -img
    - templates index.html  / base.html
    - etc

  12. En la views.py de web crear una función de respuesta http 
  views.py en la app
from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
  return HttpResponse("Hola, onlyflans")



  13. En la urls.py del proyecto anexar la route para la función previamente creada
urls.py en el project
from django.contrib import admin
from django.urls import path
from onlyflans.views import hola
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', hola)
]
  14. Modularizar la route creada (utilizando el include)

  15. Utiliza el utilitario manage.py para la creación de un nuevo proyecto Django.

  16. - .gitignore
  17. - README.md - Documentación
  18. - .env (variables de entorno)
  19. - requirements.txt
  pip freeze > requirements-onlyflans.txt
  20. Subir el proyecto a gitHub (privado)



# Requerimientos
1. python usada es python 3. Realiza un “pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un archivo jpg o png dentro de la carpeta requerimiento1.

2. Instalar django 3.2.4 dentro del entorno virtual onlyflans, una vez instalado verifica que 
haya sido instalado exitosamente utilizando el comando pip freeze. Realiza un 
“pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un 
archivo jpg o png dentro de la carpeta requerimiento2.

3. Usando django-admin genera un proyecto llamado onlyflans, una vez creado ingresa 
a la carpeta del proyecto generado, aplica las migraciones y ejecuta tu servidor 
utilizando los comandos correspondientes del archivo manage.py y accede a la url 
disponible para tu proyecto. Una vez que puedas acceder a la web en tu navegador, 
realiza un “pantallazo” de ésta y guardalo en un archivo jpg o png dentro de la carpeta
requerimiento3.
