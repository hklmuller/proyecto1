from django import forms

class LicenciadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    desempleado = forms.BooleanField(required=False)
    
class LicenciadoBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)

