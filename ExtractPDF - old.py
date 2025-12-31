import re
import PyPDF2        
pdfFileObj = open('Category4.pdf', 'rb')        
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)        

totalpages=pdfReader.numPages
page=0

while page < totalpages:
    print("////////////"+str(page+1)+"//////////")
    pageObj = pdfReader.getPage(page)        
    result = pageObj.extractText()
    #type(result)
    #print(result.split('.'))
    #print('\n')
    for line in result.split('\n'):
        #print(line)
        if re.match(r"4A\d\d\d\s", line):
            print(line)
        if re.match(r"\s4A\d\d\d\s", line):
            print(line)
        if re.match(r"\s\s4A\d\d\d\s", line):
            print(line)
    page=page+1
   
   
   

 
#for line in pages_text.split('\n'):
#    if re.match(r"_aktz: AZ x ", line):
#        print(line)
#        prefix, number = line.split('x ', 1)
#        print(number)
#        shutil.move('H:\\Scans\\TestScan\\AktzTest.pdf', f'H:\\Akten\\TestAkten\\{number}')