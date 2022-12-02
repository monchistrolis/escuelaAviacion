from django.shortcuts import render
from wedAviacion.forms import loginFormulario,registroFormulario,registroVueloFormulario
from django.http import HttpResponseRedirect

# Create your views here.

def login(request):

    if request.method == 'POST':
        form = loginFormulario(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            if usuario == "ramon" and password == "83245112":
                request.session['usuario'] = usuario
                return render(request, 'paginas/vistaAdmin.html')
    else:
        form = loginFormulario()
    return render(request,'paginas/login.html',{'form':form})

def home(request):
    return render(request, 'paginas/index.html')

def vistaAdmin(request):
    return render(request, 'paginas/vistaAdmin.html')

def workshop(request):
    return render(request, 'paginas/workshop.html')

def professionalPrograms(request):
    return render(request, 'worshop/professionalPrograms.html')

def simulatorTraining(request):
    return render(request, 'worshop/simulatorTraining.html')

def fullTimeTraining(request):
    return render(request, 'worshop/fullTimeTraining.html')

#guardar registro en la base de datos
def registro(request):
    if request.method == 'POST':
        form = registroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = registroFormulario()
    return render(request,'paginas/registro.html',{'form':form})

def registroVuelo(request):
    if request.method == 'POST':
        form = registroVueloFormulario(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'paginas/homeAdmin.html')
    else:
        form = registroVueloFormulario()
    return render(request,'paginas/registroVuelo.html',{'form':form}) 

def consultaVuelo(request):
    return render(request, 'paginas/consultaVuelo.html')

def bitacora(request):
    return render(request, 'paginas/bitacora.html')

def calendario(request):
    return render(request, 'paginas/calendario.html')