#include these libraries
import csv
import sys
from tkinter import *

#function definition
def split():
  filename = file_name.get()+".csv"
  splitrow = row_number.get()

  org = open(filename)
  csv_org = csv.reader(org)

  headers = next(csv_org)
  #headerLabel = Label(mGui,text="Existing headers in file: \n"+str(headers)).place(x=100,y=200)

  myfile = open(filename+"_A.csv", 'wt')
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  wr.writerow(headers)

  myfile2 = open(filename+"_B.csv", 'wt') #was 'wb'
  wr2 = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
  wr2.writerow(headers)

  i=0
  for row_org in csv_org:
    if i < int(splitrow)-1: #splits file after the line shown in spread sheet
      wr.writerow(row_org)
      print ("wrote row", i, "to A", " => ", i, "<", splitrow)
    else:
      wr2.writerow(row_org)
      print ("wrote row", i, "to B", " => ", i, ">", splitrow)
    i=i+1

  org.close()
  print ("The headers are: \n", headers)
  return
#end of function def

mGui = Tk()
file_name = StringVar()
row_number = IntVar()

mGui.geometry('400x250+500+300')
mGui.title('Split CSV file')

directions = Label(mGui,text="Enter File Name & row number then click RUN.").place(x=50,y=25)
directions = Label(mGui,text="(Do not include file extention.)",fg='red').place(x=50,y=45)
fileLabel = Label(mGui,text="CSV File Name:").place(x=100,y=85)
fileEntry = Entry(mGui,textvariable=file_name).place(x=100,y=105)
rowLabel = Label(mGui,text="Row Number:").place(x=100,y=135)
rowEntry = Entry(mGui,textvariable=row_number).place(x=100,y=155)
runbtn = Button(mGui,text="RUN",command=split).place(x=100,y=185)

mGui.mainloop()
