#each match row is paired with a base row
#EX: every order(base) has a customer(match) but not every customer has an order
#an extra file will be created with the skipped records for review 

import csv

match = open('../clean-formattedFiles/mergedFiles/invoiceID-orderTitle.csv')
base = open('../clean-formattedFiles/mergedFiles/SErefunds_Neg.csv')

csv_match = csv.reader(match)
csv_base = csv.reader(base)

myDict = dict()

i=0
u=0

for row_match in csv_match:
  if row_match[3] != "":
             #orderTitle = invoiceId
    myDict[row_match[3]]=(row_match[1])             #add one field from match file
    #myDict[row_match[2]]=(row_match[7],row_match[8]) #add multipule fields from match file

myfile = open("../clean-formattedFiles/mergedFiles/refunds-invoiceID.csv", 'wt')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

skippedRows = open("../clean-formattedFiles/mergedFiles/refunds-NOinvoiceID.csv", 'wt')
wrSkipped = csv.writer(skippedRows, quoting=csv.QUOTE_ALL)


for row_base in csv_base:
  if row_base[35] != "" and row_base[35] in myDict:
    add_row = myDict[row_base[35]]
    row_base.append(add_row)  #add one field to base row
    #row_base.extend(add_row)   #add multiple fields to base row
    wr.writerow(row_base)
    print ("Wrote Record: ",i)
    i=i+1
  else:
    #no base rows should be skipped.
    #EX: an order always has a customer.
    print ("Skipped Record: ",i,"customerCode=",row_base[35])
    wrSkipped.writerow(row_base)
    u=u+1
print("# of Skipped Records=",u)
   
match.close()
base.close()
