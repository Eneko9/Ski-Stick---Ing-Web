from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Estacion, Localizacion, Pista
        
def lista_estaciones_por_alquiler(request):
    ests = get_list_or_404(Estacion.objects.order_by('-puntos_alquiler'))
    locs = get_list_or_404(Localizacion)
    ests_def = []
    for e in ests:
        if e.localizacion in locs:
            ests_def.append(e)
            locs.remove(e.localizacion)
    
    context={
        'est' : ests_def
    }
    return render(request, "listaEstaciones.html", context)
    
def lista_estaciones(request):
    est = get_list_or_404(Estacion)
    context={
        'est' : est
    }
    return render(request, "listaEstaciones.html", context)

def detalle_estacion(request, id_estacion):
    det_estacion = get_object_or_404(Estacion, pk = id_estacion)
    pistas = get_list_or_404(Pista, estacion = id_estacion)
    context ={
        'det_estacion' : det_estacion,
        'pistas' : pistas
    }
    return render(request, "detalleEstacion.html", context)

def lista_localizaciones(request):
    locs = get_list_or_404(Localizacion)
    context={
        'locs' : locs
    }
    return render(request, "listaLocalizaciones.html", context)

def detalle_localizacion(request, id_localizacion):
    localizacion = get_object_or_404(Localizacion, pk = id_localizacion)
    estaciones = get_list_or_404(Estacion, localizacion = id_localizacion)
    context={
        'estaciones' : estaciones,
        'localizacion' : localizacion
    }
    return render(request, "detalleLocalizacion.html", context)

def lista_Pistas(request):
    colors = get_list_or_404(Pista)
    context={
        'colors': colors
    }
    return render(request, "listaPistas.html", context)

