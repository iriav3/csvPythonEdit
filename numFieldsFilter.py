#separate the lines that contain more fields than columns in the file and manually fix
#some rows have too many fields because the comment/notes field got split into multiple fields

import csv

base = open('../clean-formattedFiles/mergedFiles/contactAddrCC.csv')

csv_base = csv.reader(base)

myDict = dict()

i=0
u=0


myfile = open("../clean-formattedFiles/mergedFiles/contactAddrCC2Big.csv", 'wt')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

skippedRows = open("../clean-formattedFiles/mergedFiles/contactAddrCCManFix.csv", 'wt')
wrSkipped = csv.writer(skippedRows, quoting=csv.QUOTE_ALL)


for row_base in csv_base:
  num_fields = len(row_base)
  if num_fields == 24:
    wr.writerow(row_base)
    print ("Wrote Record: ",i)
    i=i+1
  else:
    print ("Skipped Record: ",i,"customerCode=",row_base[0])
    wrSkipped.writerow(row_base)
    u=u+1
print("# of Skipped Records=",u)
   
base.close()

