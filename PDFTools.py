
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader, PdfFileWriter

def PDF_merge():
    pdfs = input("Enter PDF/s names: ")
    pdfList = [pdf for pdf in pdfs.split()]
    merger = PdfFileMerger()
    print(pdfList)

    for pdf in pdfList:
        merger.append(pdf)

    merger.write("afterMerge.pdf")
    merger.close()

def PDF_separate_page():
    pdf = input("Enter PDF name: ")
    input_PDF = PdfFileReader(open(pdf, "rb"))
    page_number = input("Enter page number: ")

    output = PdfFileWriter()
    output.addPage(input_PDF.getPage(pageNumber=(int(page_number)-1)))
    with open("separatedPage.pdf", "wb") as outputStream:
        output.write(outputStream)


def PDF_delete_page():
    pdf = input("Enter PDF name: ")
    input_PDF = PdfFileReader(open(pdf, "rb"))
    page_number = input("Enter page number to delete: ")
    output = PdfFileWriter()

    for i in range(len(input_PDF.pages) ):
        if i != int(page_number):
            p = input_PDF.getPage(i)
            output.addPage(p)

    with open("afterDeletedPages.pdf", "wb") as outputStream:
        output.write(outputStream)


function = input("what function do you need?: ")
if(function == "merge"):
    PDF_merge()
elif(function == "separate"):
    PDF_separate_page()
elif(function == "delete"):
    PDF_delete_page()
    


