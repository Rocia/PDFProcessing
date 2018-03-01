from tabula import read_pdf, convert_into
import os
import pandas as pd


def readpdf(file):
    convert_into(file, file.replace(".pdf", ".json"), output_format="json")
    pdf = read_pdf(file)
    write_to_file(pdf)


def write_to_file(txt):
    df = pd.DataFrame(txt)
    #df[df.name != NaN]
    print(df)
    #txt.to_csv(file_name, encoding='utf-8', index=False)
    
    
if __name__ == '__main__':
    directory = '/root/python/Free/PDFtoText/sample/'
    names = os.listdir(directory)
    for name in names:
        readpdf(directory+name)
        print("---------------------------------------------------------------------------------", directory+name)
    
        
    
    #read_pdf(directory+'Muster Register Form II - USL Jan  18.pdf')
    