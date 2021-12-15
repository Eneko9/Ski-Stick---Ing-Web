from django import forms

from SkiStickApp.models import Estacion, Localizacion

class MyForm(forms.Form):
    valoraciones = [('1','Muy Mala'),('2','Mala'),('3','Meh'),('4','Buena'),('5','Muy Buena')]
    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    nombre_estacion = forms.ModelChoiceField(queryset=Estacion.objects.all())
    valoracion = forms.ChoiceField(widget=forms.RadioSelect, choices= valoraciones)
    opinion = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))