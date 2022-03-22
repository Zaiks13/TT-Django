from multiprocessing import context
from django.shortcuts import redirect, render

from .forms import RegistroForm
from .models import Registro
# Create your views here.


def index(request):
    lista_registro = Registro.objects.all()
    context = {
        'lista_registro': lista_registro,
    }
    return render(request, 'csv/index.html', context)


def detalleRegistro(request, id):
    registro = Registro.objects.get(pk=id)
    context = {
        'registro': registro,
    }
    return render(request, 'csv/DetalleRegistro.html', context)


def crearRegistro(request):
    form = RegistroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('csv:index')

    return render(request, 'csv/RegistroForm.html', {'form': form})


def editarRegistro(request, id):
    registro = Registro.objects.get(id=id)
    form = RegistroForm(request.POST or None, instance=registro)

    if form.is_valid():
        form.save()
        return redirect('csv:index')

    return render(request, 'csv/RegistroForm.html', {'form': form, 'registro': registro})


def eliminarRegistro(request, id):

    registro = Registro.objects.get(id=id)

    if request.method == 'POST':
        registro.delete()
        return redirect('csv:index')

    return render(request, 'csv/RegistroDelete.html', {'registro': registro})
