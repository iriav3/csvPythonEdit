#replace expdate with 2 new columns MM and YYYY from the credit card expiration date column

import csv

ccInfo = open('../SE_20160622_pmcCustomerCC.csv')
csv_ccInfo = csv.reader(ccInfo)

formatDate = open("../clean-formattedFiles/CC_SplitDate.csv", 'wt')
wr_formatDate = csv.writer(formatDate, quoting=csv.QUOTE_ALL)

iterator=0
 
for row_ccInfo in csv_ccInfo: #get row
  iterator+=1
  if iterator == 1:
      row_ccInfo[4] = "expMonth"
    row_ccInfo.insert(5, "expYear")
    wr_formatDate.writerow(row_ccInfo)
  else:
    if row_ccInfo[4]: #if expDate = true
      expDate = row_ccInfo[4]
      if len(expDate) == 3:
        expDate = "0"+expDate
      if len(expDate) == 4:
        expYear =  expDate[-2:]
        expMonth = expDate[:2]
      #update row to use new string values
      row_ccInfo[4] = expMonth
      row_ccInfo.insert(5, expYear)
      #row_ccInfo[5] = expYear
      wr_formatDate.writerow(row_ccInfo)
ccInfo.close()

