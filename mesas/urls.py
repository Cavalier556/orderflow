from django.urls import path
from . import views

urlpatterns = [
    path('mesas/', views.lista_mesas_activas, name='home'),
    path('mesas/<int:pk>/', views.mesa_detalle, name='mesa_detalle'),
    path('mesas/<int:pk>/imprimir/', views.obener_mesa_pdf),
    path('mesas/<int:pk>/add_plato/', views.add_plato),
    path('mesas/<int:pk>/detalle/<int:pk_detalle>/delete_plato/', views.delete_plato),
    path('mesas/<int:pk>/add_pago/', views.add_pago),
    path('mesas/<int:pk>/pago/<int:pk_pago>/delete_pago/', views.delete_pago),
    path('mesas/<int:pk>/archivar/', views.archivar_mesa),

    path('ventas/', views.lista_archivo, name='archivo'),
     path('reporte/', views.ver_reporte, name='reporte'),
]