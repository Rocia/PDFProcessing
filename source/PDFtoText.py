import PyPDF2
import sys, glob, os


def read_pdf(file):
    pdf_file = open(file, 'rb')
    pdf = PyPDF2.PdfFileReader(pdf_file)
    data = text_process(pdf)
    return data
    
def text_process(pdf):
    text = ''
    for i in range(0,  pdf.getNumPages()):
        pg = pdf.getPage(i)
        data = pg.extractText()
        text = text + data
    print(text)
    return text
    
if __name__ == '__main__':
    directory = '/root/python/Free/PDFtoText/sample/'
    names = os.listdir(directory)
    for name in names:
        text = read_pdf(directory+name)
        print("---------------------------------------------------------------------------------")
        
    
    #read_pdf(directory+'Muster Register Form II - USL Jan  18.pdf')
    