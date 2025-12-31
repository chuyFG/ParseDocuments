from docx import *
import re

doclist=['Category1.docx','Category2.docx','Category3.docx','Category4.docx','Category5Part1.docx','Category5Part2.docx','Category6.docx','Category7.docx']


for item in doclist:
    document = Document(item)
    bolds=[]
    italics=[]
    for para in document.paragraphs:
        for run in para.runs:
            #if run.italic :
            #    italics.append(run.text)
            if run.bold :
                bolds.append(run.text)
              
    #print(bolds)
    for line in bolds:
            #print(line)
            if re.match(r"\dA\d\d\d\s", line):
                print(line)
            if re.match(r"\s\dA\d\d\d\s", line):
                print(line)
            if re.match(r"\s\s\dA\d\d\d\s", line):
                print(line)
            if re.match(r"\dB\d\d\d\s", line):
                print(line)
            if re.match(r"\s\dB\d\d\d\s", line):
                print(line)
            if re.match(r"\s\s\dB\d\d\d\s", line):
                print(line)
            if re.match(r"\dC\d\d\d\s", line):
                print(line)
            if re.match(r"\s\dC\d\d\d\s", line):
                print(line)
            if re.match(r"\s\s\dC\d\d\d\s", line):
                print(line)
            if re.match(r"\dD\d\d\d\s", line):
                print(line)
            if re.match(r"\s\dD\d\d\d\s", line):
                print(line)
            if re.match(r"\s\s\dD\d\d\d\s", line):
                print(line)
            if re.match(r"\dE\d\d\d\s", line):
                print(line)
            if re.match(r"\s\dE\d\d\d\s", line):
                print(line)
            if re.match(r"\s\s\dE\d\d\d\s", line):
                print(line)