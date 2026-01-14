# OrderFlow

**OrderFlow** es un sistema de gestión de ventas (POS) de código abierto diseñado específicamente para optimizar la operación de restaurantes, cafeterías y otros negocios gastronómicos.

## Características principaless
* **Gestión de Mesas:** Visualiza las mesas activas y el monto total pendiente.
* **Gestión de Platillos:** Crea platillos para tenerlos en tu menú.
* **Impresión de Pedidos:** Obtén un PDF en tamaño tiquetera para imprimirlos rápidamente.
* **Registro de Pagos:** Crea tipos de pagos e ingresa los pagos recibidos para las mesas.
* **Archivado de Pedidos:** Archiva las mesas pagadas para verlas en el historial de ventas.

## Configuración
* Crea tu archivo .env con las siguientes variables SECRET_KEY, NOMBRE y DIRECCION
* Crea tu superuser para poder ingresar al sistema
```
python manage.py createsuperuser
```
* Ingresa al sistema y dirigite a /admin/ para crear usuarios adicionales e información como Tipos de Pagos

## Tecnologías utilizadas
* **Django**
* **SQLite**
* **TailwindCSS**
* **HTMX**
* **FPDF**