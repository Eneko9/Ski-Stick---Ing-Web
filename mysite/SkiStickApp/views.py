from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse

from SkiStickApp.forms import MyForm
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
    return render(request, "home.html", context)
    
def lista_estaciones(request):
    est = get_list_or_404(Estacion)
    context={
        'est' : est
    }
    return render(request, "listaEstaciones.html", context)

def detalle_estacion(request, id_estacion):

    det_estacion = get_object_or_404(Estacion, pk = id_estacion)

    context ={
        'det_estacion' : det_estacion
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

#devuelve la imagen de una localización 
def detalle_localizacion_ajax(request, id_localizacion):
    localizacion = get_object_or_404(Localizacion, pk = id_localizacion)
    estaciones = get_list_or_404(Estacion, localizacion = id_localizacion)
    context={
        'estaciones' : estaciones,
        'localizacion' : localizacion
    }
    return render(request, "detalleLocalizacionAjax.html", context)
def lista_pistas(request):
    colors = get_list_or_404(Pista)
    colors2 = []
    for c in colors:
        if c.color_tipo not in colors2:
            colors2.append(c.color_tipo)
    
    context={
        'colors2': colors2
    }
    return render(request, "listaPistas.html", context)


def detalle_pista(request, color_tipo):

    det_pista = get_object_or_404(Pista, color_tipo = color_tipo)

    context ={
        'det_pista' : det_pista
    }
    return render(request, "detallePista.html", context)

def opinionForm(request):
    form = MyForm()
    return render(request, "opiniones.html", {'form': form})    