from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from Coordenadas.models import Ruta

# Create your views here.

def ingresoCoordenadas(request):
    if ('Lat' not in request.GET) or ('Lon' not in request.GET):
        return HttpResponseNotFound('<center><h1>Error petición invalida</h1></center>')
    
    else:
        Lat = float(request.GET['Lat'])
        Lon = float(request.GET['Lon'])
        User = int(request.GET['User'])

        Ruta.objects.create(idUser = User, latitud = Lat, longitud = Lon)

        return HttpResponse('<center><h1>OK</h1></center>', status = 200)