#This file formats an exsisting date field 20160422 to 2016-04-22
#This needs to be run on the orders and refunds or on the single file before they are split.

import csv

orders = open('../SE_20160622_pmcCbauditRevised.csv')
csv_orders = csv.reader(orders)

formatDate = open("../clean-formattedFiles/purchasesGoodDates.csv", 'wt')
wr_formatDate = csv.writer(formatDate, quoting=csv.QUOTE_ALL)

iterator=0
 
for row_orders in csv_orders: #get row
  iterator+=1
  if iterator == 1:
    wr_formatDate.writerow(row_orders)
  else:
    if row_orders[10]: #dateOfTx -- format string to date
      dateOfTx = row_orders[10]
      newDateOfTx = dateOfTx[:4] + "-" + dateOfTx[4:6] + "-" + dateOfTx[-2:]
      if row_orders[11]: #dateOfUpdate -- format string to date
        dateOfUpdate = row_orders[11]
        newDateOfUpdate = dateOfUpdate[:4] + "-" + dateOfUpdate[4:6] + "-" + dateOfUpdate[-2:]
      #change row to use new string values
      row_orders[10] = newDateOfTx
      row_orders[11] = newDateOfUpdate 
      wr_formatDate.writerow(row_orders)
orders.close()

