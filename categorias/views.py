from django.shortcuts import render, redirect
from .models import Categoria
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def categorias(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        url = request.headers.get('HX-Current-URL')
        return redirect(url)
    categorias = Categoria.objects.order_by('nombre').all()
    return render(request, 'categorias/index.jinja2', {'categorias': categorias})