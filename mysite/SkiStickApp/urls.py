from django.urls import path
from . import views
urlpatterns = [
    #SkiStickApp/
    path('', views.lista_estaciones_por_alquiler, name='home'),
    #SkiStickApp/estaciones
    path('estaciones', views.lista_estaciones, name='estaciones'),
    #SkiStickApp/localizaciones
    path('localizaciones', views.lista_localizaciones, name='localizaciones'),
    #SkiStickApp/pistas
    path('pistas', views.lista_pistas, name='pistas'),
    #SkiStickApp/estaciones/<id>
    path('estaciones/<int:id_estacion>', views.detalle_estacion, name='detalles_est'),
    #SkiStickApp/localizaciones/<id>
    path('localizaciones/<int:id_localizacion>', views.detalle_localizacion, name='detalles_localizacion'),
    #SkiStickApp/localizacionesAjax/<id>
    path('localizacionesAjax/<int:id_localizacion>', views.detalle_localizacion_ajax, name = 'ajax'),
    #SkiStickApp/pistas/<color>
    path('pistas/<str:color_tipo>', views.detalle_pista, name= 'detalles_pista'),
    #SkiStickApp/opiniones
    path('opiniones', views.opinionForm, name = 'opiniones')
]
