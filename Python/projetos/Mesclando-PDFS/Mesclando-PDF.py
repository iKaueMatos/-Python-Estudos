import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

lista_arquivos = os.listdir('pdfs')






merger.append('Exemplo-de-pdf.pdf')