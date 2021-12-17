from django import forms

from SkiStickApp.models import Estacion, Opinion
from django.forms import ModelForm

class MyForm(forms.Form):
    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    nombre_estacion = forms.ModelChoiceField(queryset=Estacion.objects.all())
    valoracion = forms.IntegerField(min_value=1, max_value=5)
    opinion = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))


class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = '__all__'