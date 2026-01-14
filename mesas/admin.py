from django.contrib import admin
from .models import Mesa, MesaDetalle, Pago

# Register your models here.
admin.site.register(Mesa)
admin.site.register(MesaDetalle)
admin.site.register(Pago)