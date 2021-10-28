import pyttsx3
import PyPDF2

open_pdf = open('Zahid Hassan QA.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(open_pdf)
print(pdf_reader.numPages)
friend = pyttsx3.init()
page = pdf_reader.getPage(0)
text = page.extractText()
friend.say(text)
friend.runAndWait()
