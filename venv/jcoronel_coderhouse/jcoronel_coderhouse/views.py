from ctypes import HRESULT
from curses.ascii import HT
from re import T
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def primer_vista(request):
    nombre = "Javier"
    apellido = "Coronel"
    lista = [1,2,3,10,9,8,10,10,1,2,3,4]
    dict_context = {"nombre" : nombre, "apellido" : apellido , "listado" : lista}
    archivo = open(r"C:\Users\javie\OneDrive\Documentos\django-intro\venv\jcoronel_coderhouse\jcoronel_coderhouse\templates\inicio.html", 'r')
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context(dict_context)
    documento = plantilla.render(contexto)
    return  HttpResponse (documento)

def segunda_vista(request):
    date = datetime.now()
    return  HttpResponse (f"<h1> Hello word from my second view in Django, date data: {date}</h1>")

def nombre_usuario(request, nombre):
    return HttpResponse(f"Tu nombre es {nombre}")

def año_nacimiento(request, edad):
    nacimiento = int(datetime.today().year) - int( edad )   
    return HttpResponse(f"naciste en el año {nacimiento}")