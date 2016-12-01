#Removes most of the following from each field in a row: commas, the special null value of "\N" and new lines

#if part of a row is seen by Python as a complete row then the partial rows get a little messy
#first run to get error and find partial row problem line# then run again
#mannually change the weird rows in newly created file or add code to move them to another file ... maybe with a try/catch 

#OR use the Ruby script instead

import csv

badChars = open('../../SE_20160622_pmcCustomer.csv')
csv_badChars = csv.reader(badChars)

goodChars = open("../customerClean.csv", 'wt')
wr_goodChars = csv.writer(goodChars, quoting=csv.QUOTE_ALL)

#skipped = open("../skipped.csv", 'wt')
#wr_skipped = csv.writer(skipped, quoting=csv.QUOTE_ALL)

iterator=0
 
for row_badChars in csv_badChars: #get row
  iterator+=1
  if iterator == 1:
    wr_goodChars.writerow(row_badChars)

  else:
    row_length = len(row_badChars)-1

    if row_length!=9: #expected field count starting at zero
      print("row# = ",iterator," & ","row_length = ",row_length)
      print(row_badChars)
      print()
      row_length=9

    for i in range (0,row_length):
      if ',' in row_badChars[i]:
        str_badChars = row_badChars[i].replace(",","")
        row_badChars[i] = str_badChars

      if r'\N' in row_badChars[i]:
        str_badChars = row_badChars[i].replace(r"\N","")
        row_badChars[i] = str_badChars

      if r'\n' in row_badChars[i]:
        str_badChars = row_badChars[i].replace(r"\n","")
        row_badChars[i] = str_badChars

    wr_goodChars.writerow(row_badChars)

badChars.close()

