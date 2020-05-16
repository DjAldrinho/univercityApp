from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from biblioteca.models import Libro, Tesis, Revista, MaterialBibliografico, Categoria, Cliente, Reserva

from biblioteca.forms import ReservaForm, ClienteForm


def login(request):
    if request.method == 'GET':
        if request.session.exists('email'):
            return redirect("index")
        else:
            return render(request, 'biblioteca/login.html', {})
    else:
        correo = request.POST['email']
        password = request.POST['password']
        cliente = Cliente.objects.filter(correo=correo, password=password)
        if cliente:
            correo = request.POST['email']
            request.session['email'] = correo
            request.session['id_cliente'] = cliente.get().id
            return redirect("index")
        else:
            return redirect("login")


def logout(request):
    try:
        request.session['email'] = ''
    except:
        pass
    return redirect("login")


def registro(request):
    if request.method == 'GET':
        if request.session.exists('email'):
            return redirect("index")
        else:
            form = ClienteForm(request.GET)
            return render(request, 'biblioteca/registrarse.html',
                          {'form': form})

    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            messages.success(request, "Has sido registrado correctamente!")
            form.save()
            return redirect(reverse('registro'))
        else:
            return HttpResponse("Hubo un error")


def index(request):
    codigo = ''
    titulo = ''
    categoria = ''
    if request.method == 'GET':
        libros = Libro.objects.filter(estado='A')
        tesis = Tesis.objects.filter(estado='A')
        revistas = Revista.objects.filter(estado='A')
    else:
        filtros = {'estado': 'A'}

        codigo = request.POST.get('codigo')
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')

        if request.POST.get('categoria'):
            filtros['categoria'] = categoria
        elif request.POST.get('codigo'):
            codigo = request.POST.get('codigo')
            filtros['codigo__icontains'] = codigo
        elif request.POST.get('titulo'):
            titulo = request.POST.get('titulo')
            filtros['titulo__icontains'] = titulo

        libros = Libro.objects.filter(**filtros)
        tesis = Tesis.objects.filter(**filtros)
        revistas = Revista.objects.filter(**filtros)

    categorias = Categoria.objects.filter(estado='A')

    if len(request.session.get('email')) > 0:
        return render(
            request,
            'index.html',
            context={'libros': libros, 'tesis': tesis, 'revistas': revistas, 'categorias': categorias,
                     'categoria': categoria, 'codigo': codigo, 'titulo': titulo},
        )
    else:
        return redirect("login")


def detalle(request, tipo, pk):
    if tipo == 'libro':
        model = get_object_or_404(Libro, pk=pk)
    elif tipo == "revista":
        model = get_object_or_404(Revista, pk=pk)
    else:
        model = get_object_or_404(Tesis, pk=pk)

    return render(request, 'biblioteca/reservas/detalle.html',
                  {'model': model})


def get_reserva(request, pk):
    form = ReservaForm(request.GET)
    return render(request, 'biblioteca/reservas/reservar.html',
                  {'material': pk, 'form': form})


def reservar(request):
    reserva = Reserva()
    material = get_object_or_404(MaterialBibliografico, pk=request.POST['material'])
    cliente = get_object_or_404(Cliente, pk=request.POST['usuario'])
    reserva.save()
    reserva.material = material
    reserva.cliente = cliente
    material.cantidad = material.cantidad - 1
    reserva.fecha_creacion = timezone.now()
    reserva.estado = 'P'
    reserva.save()
    material.save()
    messages.success(request, "Tu reserva ha sido generada exitosamente!")
    return redirect(reverse('index'))
