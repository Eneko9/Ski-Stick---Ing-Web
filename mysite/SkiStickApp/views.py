from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Estacion, Localizacion, Pista

# Create your views here

#def lista_estaciones_por_alquiler(request):
    #ests = []
    #ests1 = []
    #locs = get_list_or_404(Localizacion)
    #for l in locs:
        #ests1.append(get_object_or_404(Estacion, localizacion = l.id))
        #for e in ests1:
            #ests.append(get_object_or_404(Estacion, e.puntos_alquiler = max(ests1.puntos_alquiler)))
        


def lista_estaciones(request):
    est = get_list_or_404(Estacion)
    context={
        'est' : est
    }
    return render(request, "index.html", context)

def detalle_estacion(request, id_estacion):
    det_estacion = get_object_or_404(Estacion, id = id_estacion)
    pistas = get_list_or_404(Pista)
    context ={
        'det_estacion' : det_estacion,
        'pistas' : pistas
    }
    return render(request, "index.html", context)

def lista_localizaciones(request):
    locs = get_list_or_404(Localizacion)
    context={
        'locs' : locs
    }
    return render(request, "index.html", context)

def detalle_localizacion(request, id_localizacion):
    pistas = []
    estaciones = get_list_or_404(Estacion, localizacion = id_localizacion)
    for e in estaciones:
        pistas.append(get_object_or_404(Pista, estacion=e.id))
    context={
        'pist' : pistas
    }
    return render(request, "index.html", context)
