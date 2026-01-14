from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Categoria, Plato

# Create your views here.
@login_required
def platos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(pk=categoria_id)
        precio = request.POST.get('precio')
        Plato.objects.create(nombre=nombre,categoria=categoria,precio=precio)

    categorias = Categoria.objects.all()
    platos = Plato.objects.all()

    context = {
        'categorias': categorias,
        'platos': platos,
    }

    return render(request,'platos/index.jinja2', context)