import os
from tika import parser


def readpdf(file):
    parsedPDF = parser.from_file(file)
    write_to_file(parsedPDF, file)



def write_to_file(txt, filename):
    print(txt.keys())
    with open (filename+'.csv', 'w') as f:
        f.write(txt["content"])
    
    
if __name__ == '__main__':
    directory = '/root/python/Free/PDFtoText/sample/'
    names = os.listdir(directory)
    for name in names:
        print(directory+name)
        readpdf(directory+name)
        print("---------------------------------------------------------------------------------")
'''        
from tika import parser
parsedPDF = parser.from_file('/root/python/Free/PDFtoText/sample/MLWF Challan December 2017 Be3.pdf')
def create_df(pdf_content, content_pattern, line_pattern, column_headings):

    list_of_line_items = []
    content_match = re.search(content_pattern, pdf_content, re.DOTALL)
    content_match = content_match.group(1)
    content_match = content_match.split('\n')
    for item in content_match:
        line_items = []
        line_match = re.search(line_pattern, item, re.I)
        agency = line_match.group(1).strip().replace(',', '')
        values_string = line_match.group(2).strip().\
        replace('- ', '0.0 ').replace('$', '').replace(',', '')
        values = map(float, values_string.split())
        line_items.append(agency)
        line_items.extend(values)
        list_of_line_items.append(line_items)
    df = pd.DataFrame(list_of_line_items, columns=column_headings)
    return df

#create_df(parsedPDF)
def write_to_file(txt):
    print(txt.keys())
    with open ('a.csv', 'w') as f:
        f.write(txt["content"])



write_to_file(parsedPDF)
        '''
