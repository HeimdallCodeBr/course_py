import pathlib

import PyPDF2 as pyf

pdf_mesclado = pyf.PdfFileMerger()

arquivo1 = "Partilha01.pdf"
arquivo2 = "Partilha02.pdf"

pdf_mesclado.append(arquivo1)
pdf_mesclado.append(arquivo2)


with pathlib.Path('Consolidado.pdf').open(mode='wb') as arquivo_final:
    pdf_mesclado.write(arquivo_final)
