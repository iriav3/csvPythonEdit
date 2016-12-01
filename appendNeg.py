#prepend a '-' to a specific field of every row, EVEN THE HEADER

import csv

base = open('../clean-formattedFiles/mergedFiles/SErefunds.csv')

csv_base = csv.reader(base)

i=0
u=0

myfile = open("../clean-formattedFiles/mergedFiles/SErefunds_Neg.csv", 'wt')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

for row_base in csv_base:
  oldFieldValue = row_base[13]
  newFieldValue = "-"+oldFieldValue
  row_base[13] = newFieldValue
  wr.writerow(row_base)
  print ("Wrote Record: ",i)
  i=i+1
   
base.close()

