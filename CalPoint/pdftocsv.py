import tabula
#import PyPDF2

#pdfFileObj = open('FIRSTSEMMARKS.pdf', 'rb') 
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#tot_pages = pdfReader.numPages 
#print("Total number of pages in pdf: ",pdfReader.numPages) 

name = "FIRSTSEMMARKS.pdf"
tables = tabula.read_pdf(name,pages = "all",multiple_tables=True)
print(tables)
ankit = []
ankit.append(tables)
#print(len(ankit))
#print(ankit[0][1])
#for i in ankit[0]:
#	print(i.loc[0])