from django.shortcuts import redirect, render
from .models import Licenciado
from .forms import LicenciadoFormulario, LicenciadoBusqueda

# Create your views here.

def crear_licenciado(request):
    
    if request.method == 'POST':
        form = LicenciadoFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            licenciado = Licenciado(nombre=data['nombre'], apellido=data['apellido'], desempleado=data['desempleado'])
            licenciado.save()
            return redirect('index')
            
    
    form = LicenciadoFormulario()
    return render(request, "profesiones/crear_licenciado.html", {'form': form})

def lista_licenciado(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        licenciado = Licenciado.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        licenciado = Licenciado.objects.all()
        
    form = LicenciadoBusqueda()
    return render(request, "profesiones/lista_licenciado.html", {'form': form, 'Licenciados': Licenciado})
    
