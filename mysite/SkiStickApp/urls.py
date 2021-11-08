from django.urls import path
from . import views
urlpatterns = [
    #SkiStickApp/estaciones
    path('estaciones', views.lista_estaciones, name='estaciones'),
    path('localizaciones', views.lista_localizaciones, name='localizaciones'),
    path('estaciones/<int:id_estacion>', views.detalle_estacion, name='detalles_est'),
    path('localizaciones/<int:id_localizacion>', views.detalle_localizacion, name='detalles_localizacion')
]
