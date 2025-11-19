from fpdf import FPDF
import os

path = os.path.dirname(os.path.abspath(__file__))

pdf = FPDF()
pdf.add_page()
pdf.set_font('ARIAL', size=12)

pdf.cell(200, 10, txt="Hola mundo desde un PDF.", ln=True, align='C')
pdf.cell(200, 10, txt="PDF generado por Python.", ln=True, align='C')

pdf.output(f"{ path }/fileFolder/archivo.pdf")