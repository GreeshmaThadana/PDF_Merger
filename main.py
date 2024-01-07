import PyPDF2
from PyPDF2 import PdfFileMerger

pdfs = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()
for items in pdfs:
    pdffile = open(items, "rb")
    pdfreader = PyPDF2.PdfReader(pdffile)
    merger.append(pdfreader)
    pdffile.close()
merger.write("merged.pdf")
