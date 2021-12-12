from django import forms

class MyForm(forms.Form):

    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    nombre_estacion = forms.CharField(label='Introduce estacion', max_length=100)
    opinion = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))