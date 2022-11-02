import pyttsx3
import PyPDF2
book=open("C:/Users/HP/OneDrive/Desktop/Python-Programs/object_oriented_python_tutorial.pdf","rb")
reader=PyPDF2.PdfFileReader(book)
pages=reader.numPages
print(pages)
s=pyttsx3.init() #this line makes speaker.
for num in range(0,pages): #takes page on index wise not page no.wise.
    page=reader.getPage(num)
    text=page.extractText()
    s.say(text)
    s.runAndWait()

#oop=
#abstraction=
#encapulation=