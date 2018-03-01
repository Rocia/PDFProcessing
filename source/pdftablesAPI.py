import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
filename  = '/root/python/Free/PDFtoText/sample/MLWF Challan December 2017 Be3'
htmlfile = open(filename+'.html', 'w+')
files = {'f': (filename+'.pdf', open(filename+'.pdf', 'rb'))}
response = requests.post('https://pdftables.com/api?key=r4i5cvh74tvn', files=files)
response.raise_for_status() # ensure we notice bad responses
for chunk in response.iter_content(chunk_size=1024):
    if chunk:
        htmlfile.write(chunk)
    htmlfile.flush()
htmlfile.close()
