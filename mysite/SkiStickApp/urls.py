from django.urls import path
from . import views
urlpatterns = [
    #SkiStickApp/estaciones
    path('', views.lista_estaciones_por_alquiler, name='estaciones_alq'),
    path('estaciones', views.lista_estaciones, name='estaciones'),
    path('localizaciones', views.lista_localizaciones, name='localizaciones'),
    path('pistas', views.lista_pistas, name='pistas'),
    path('estaciones/<int:id_estacion>', views.detalle_estacion, name='detalles_est'),
    path('localizaciones/<int:id_localizacion>', views.detalle_localizacion, name='detalles_localizacion'),
    path('pistas/<str:color_tipo>', views.detalle_pista, name= 'detalles_pista')
]
