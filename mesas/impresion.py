import time
import environ
from fpdf import FPDF

env = environ.Env()
environ.Env.read_env()

def obtener_pdf(data):
    t = time.localtime()
    fecha = time.strftime("%d/%m/%Y %H:%M", t)

    pdf = FPDF("P", "mm", (80, 200))
    pdf.add_page()
    pdf.set_margins(5, 5, 5)
    pdf.set_font("helvetica", "b", 14.0)
    pdf.multi_cell(60, 6, env('NOMBRE'), 0, "C")
    pdf.set_font("helvetica", "", 9.0)
    pdf.multi_cell(70, 5, env('DIRECCION'), 0, "C")
    pdf.cell(
        70,
        2,
        "-----------------------------------------------------------------",
        0,
        1,
        "L",
    )
    pdf.set_font("helvetica", "b", 9.0)
    pdf.multi_cell(70, 5, "CUENTA", 0, "C")
    pdf.cell(
        70,
        2,
        "-----------------------------------------------------------------",
        0,
        1,
        "L",
    )
    pdf.set_font("helvetica", "", 9.0)
    pdf.cell(5, 4, "Qt.", 0, 0, "L")
    pdf.cell(35, 4, "Nombre", 0, 0, "L")
    pdf.cell(15, 4, "Precio", 0, 0, "L")
    pdf.cell(15, 4, "Importe", 0, 1, "L")
    pdf.cell(
        70,
        2,
        "-----------------------------------------------------------------",
        0,
        1,
        "L",
    )

    pdf.set_font("helvetica", "", 7.0)
    total = 0
    total_productos = 0
    for articulo in data:
        pdf.cell(5, 4, f"{articulo.cantidad}", 0, 0, "L")
        y_inicio = pdf.get_y()
        pdf.multi_cell(35, 4, f"{articulo.plato.nombre}", 0, "L")
        y_final = pdf.get_y()
        pdf.set_xy(45, y_inicio)
        pdf.cell(15, 4, f"S/{format(articulo.precio, '.2f')}", 0, 0, "L")
        importe = articulo.precio * articulo.cantidad
        total += importe
        total_productos += articulo.cantidad
        pdf.cell(15, 4, f"S/{format(importe, '.2f')}", 0, 1, "L")
        pdf.set_y(y_final)

    pdf.set_font("helvetica", "b", 9.0)
    pdf.cell(
        70,
        2,
        "-----------------------------------------------------------------",
        0,
        1,
        "L",
    )
    pdf.set_font("helvetica", "b", 14.0)
    pdf.cell(70, 8, f"Total: S/{format(total, '.2f')}", 0, 1, "R")
    pdf.set_font("helvetica", "", 9.0)
    pdf.cell(70, 5, f"Total de productos: {total_productos}", 0, 1, "L")
    pdf.cell(
        70,
        2,
        "-----------------------------------------------------------------",
        0,
        1,
        "L",
    )
    pdf.cell(70, 5, f"Numero de mesa: {data[0].mesa.numero}", 0, 1, "L")
    pdf.cell(70, 5, f"Fecha: {fecha}", 0, 1, "L")
    pdf.cell(70, 8, "Notas:", 0, 1, "L")
    pdf.cell(70, 30, "", 0, 1, "L")
    pdf.cell(
        70,
        2,
        "-----------------------------------------------------------------",
        0,
        1,
        "L",
    )

    pdf.output("output.pdf", "F")