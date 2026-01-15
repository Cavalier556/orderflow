from django.db import models
from platos.models import Plato
from tipopagos.models import TipoPago

# Create your models here.
class Mesa(models.Model):
    numero = models.CharField(max_length=5)
    pagada = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    notas = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        string = f'{self.fecha} | {self.numero}'
        return string

class MesaDetalle(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)

    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        string = f'{self.mesa.numero} | {self.cantidad}x {self.plato.nombre}'
        return string

class Pago(models.Model):
    tipo = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = f'{self.fecha} | {self.tipo.nombre} | {self.monto}'
        return string