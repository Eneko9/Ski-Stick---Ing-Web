from django.urls import path
from . import views
urlpatterns = [
    #SkiStickApp/estaciones
    path('estaciones', views.lista_estaciones, name='estaciones'),
    path('localizaciones', views.lista_localizaciones, name='localizaciones'),
    path('<int:id_estacion>', views.detalle_estacion, name='detalles_est'),
]