from django.contrib import admin
from.models import Localizacion, Estacion, Pista, Opinion

# Register your models here.
admin.site.register(Estacion)
admin.site.register(Localizacion)
admin.site.register(Pista)
admin.site.register(Opinion)