from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
#from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
#from pdfminer.pdfparser import PDFParser
path_pdf='C:/Users/HP/OneDrive/Desktop/Python-Programs/object_oriented_python_tutorial.pdf'
resource_manager=PDFResourceManager(caching=True)
out_text=StringIO()
laParams=LAParams()
text_converter=TextConverter(resource_manager,out_text,laparams=laParams)
fp=open(path_pdf,'rb')
interpreter=PDFPageInterpreter(resource_manager,text_converter)
for page in PDFPage.get_pages(fp,pagenos=set(),maxpages=0,password="",caching=True,check_extractable=True):
    interpreter.process_page(page)
text=out_text.getvalue()
fp.close()
text_converter.close()
out_text.close()
print(text)