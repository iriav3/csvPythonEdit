#each match row is paired with a base row
#EX: every order(base) has a customer(match) but not every customer has an order
#an extra file will be created with the skipped records for review 

#special: it combines 2 fields for the key in the dictionary

import csv

match = open('../clean-formattedFiles/mergedFiles/exportOrders.csv')
base = open('../clean-formattedFiles/mergedFiles/exportInvoices.csv')

csv_match = csv.reader(match)
csv_base = csv.reader(base)

myDict = dict()

i=0
u=0

for row_match in csv_match:
  if row_match[0] != "":
          #customerCode = customerId
    myDict[row_match[0]+row_match[2]]=(row_match[1])
   #myDict[row_match[1]]=(row_match[0],row_match[1],row_match[2]) #adding more fields from match file

myfile = open("../clean-formattedFiles/mergedFiles/invoiceID-orderTitle.csv", 'wt')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

skippedRows = open("../clean-formattedFiles/mergedFiles/invoices-NoTitle.csv", 'wt')
wrSkipped = csv.writer(skippedRows, quoting=csv.QUOTE_ALL)


for row_base in csv_base:
  if row_base[2] != "" and row_base[0] != "" and row_base[2]+row_base[0] in myDict:
    add_row = myDict[row_base[2]+row_base[0]]
    #row_base.extend(add_row) #adding more than one field to each base row
    row_base.append(add_row)  #adding adding only one field to base row
    wr.writerow(row_base)
    print ("Wrote Record: ",i)
    i=i+1
  else:
    #no base rows should be skipped.
    #EX: an order always has a customer.
    print ("Skipped Record: ",i,"contactId=",row_base[2])
    wrSkipped.writerow(row_base)
    u=u+1
print("# of Skipped Records=",u)
   
match.close()
base.close()
