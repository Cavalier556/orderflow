from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_http_methods
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mesa, MesaDetalle, Plato, Pago
from tipopagos.models import TipoPago

from .impresion import obtener_pdf

# Create your views here.
@login_required
def home(request):
    return render(request,'home.jinja2')

@login_required
def lista_mesas_activas(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        Mesa.objects.create(numero=numero)
    mesas = Mesa.objects.filter(pagada=False).order_by('numero')

    total_consulta = MesaDetalle.objects.filter(
        mesa__in=mesas
    ).aggregate(
        total_general=Sum(F('precio') * F('cantidad'))
    )
    total = total_consulta['total_general'] or 0

    context = {
        'mesas': mesas,
        'total': total,
    }

    return render(request, 'mesas/index.jinja2', context)

@login_required
def mesa_detalle(request, pk):
    if request.method == 'DELETE':
        mesa = Mesa.objects.get(pk=pk).delete()
        return redirect('home')
    mesa = Mesa.objects.get(pk=pk)
    all_platos = Plato.objects.all()
    platos = MesaDetalle.objects.filter(mesa=pk)
    tipopagos = TipoPago.objects.all()


    pagos = Pago.objects.filter(mesa_id=pk).all()
    pagos_consulta = pagos.aggregate(
        total_pagado=Sum('monto')
    )

    total_pagado = pagos_consulta['total_pagado'] or 0

    total_consulta = platos.aggregate(
        total_pagar=Sum(F('precio') * F('cantidad'))
    )
    total = total_consulta['total_pagar'] or 0

    context = {
        'mesa': mesa,
        'all_platos': all_platos, 
        'platos': platos,
        'total': total,
        'tipopagos': tipopagos,
        'pagos':pagos,
        'restante': total - total_pagado,
    }

    return render(request, 'mesas/detalle.jinja2', context)

def obener_mesa_pdf(request, pk):
    mesa = Mesa.objects.get(pk=pk)
    platos = MesaDetalle.objects.filter(mesa=pk)
    if platos:
        obtener_pdf(platos)
    return FileResponse(open('output.pdf', 'rb'), as_attachment=False, content_type='application/pdf')

@login_required
def archivar_mesa(request, pk):
    mesa = Mesa.objects.get(id=pk)
    mesa.pagada = True
    mesa.save()
    response = HttpResponse(status=303) # No Content
    response['HX-Redirect'] = '/mesas/'
    return response

@require_http_methods(["POST"])
def add_plato(request, pk):
    mesa = Mesa.objects.get(id=pk)
    plato = Plato.objects.get(id=request.POST.get('plato_nuevo'))
    precio = request.POST.get('precio')
    cantidad = request.POST.get('cantidad')
    MesaDetalle.objects.create(mesa=mesa,plato=plato,precio=precio,cantidad=cantidad)
    return redirect('mesa_detalle', pk=pk)

@require_http_methods(["POST"])
def add_pago(request, pk):
    mesa = Mesa.objects.get(id=pk)
    tipo = TipoPago.objects.get(id=request.POST.get('tipopago'))
    monto = request.POST.get('monto')
    Pago.objects.create(tipo= tipo, mesa=mesa, monto= monto)
    return redirect('mesa_detalle', pk=pk)

@require_http_methods(["DELETE"])
def delete_plato(request, pk, pk_detalle):
    detalle = MesaDetalle.objects.get(id=pk_detalle)
    detalle.delete()
    response = HttpResponse(status=303) # No Content
    response['HX-Redirect'] = f'/mesas/{pk}/'
    return response

@require_http_methods(["DELETE"])
def delete_pago(request, pk, pk_pago):
    pago = Pago.objects.get(id=pk_pago)
    pago.delete()
    response = HttpResponse(status=303) # No Content
    response['HX-Redirect'] = f'/mesas/{pk}/'
    return response