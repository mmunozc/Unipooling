
from contextlib import ContextDecorator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import RutaForm, MyUserCreationForm, vehiculoForm


def home(request):
    return render(request, 'home.html')


def principal(request): 
    return render(request, 'principal.html')


def horario(request): 
    context = {
        "horarios" : User.objects.all()
    }
    return render(request, 'horario.html', context)


def vehiculo(request): 
        if request.method == 'POST':
            formr = vehiculoForm(request.POST)
            if formr.is_valid():
                formr.instance.user = request.user
                formr.save()
                messages.success(request, 'Se ha registrado tu vehiculo')
                return redirect('principal') 
            else:
                messages.success(request, 'Verifica tus datos')
        else:
            formr =vehiculoForm()

        return render(request, 'vehiculoh.html', context={"formr": formr}) 


def datos(request):
    return render(request, 'datos.html')

def register(request):
    form = MyUserCreationForm()
    if request.method=='POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username= user.username.lower()
            user.save()            
            return redirect('principal')
        else: 
            messages.error(request, 'An error occurred during registration')
    
    return render(request,'register.html', { 'form' : form})

def rutas(request):
    Rutas = Ruta.objects.all()
    context = {'rutas': Rutas}
    return render(request, 'ruta.html', context)


def registrarRutaView(request, *args, **kwargs):
    if request.method == 'POST':
        formr = RutaForm(request.POST)
        if formr.is_valid():
            formr.instance.user = request.user
            formr.save()
            messages.success(request, 'Se ha registrado tu vehiculo')
            return redirect('principal') 
        else:
            messages.success(request, 'Verifica tus datos')
    else:
        formr =RutaForm()

    context = {'formr': formr, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'registrarRuta.html',context ) 

def datosVehiculo(request, pk):
    logged_in_user_vehiculo = Vehiculo.objects.filter(user_id=pk)
    return render(request, 'datosVehiculo.html', {'vehiculo': logged_in_user_vehiculo})

def contacto(request, pk):
    instance = get_object_or_404(Ruta, id=pk)
    context={'Creador': instance}
    return render(request,'contacto.html', context) 