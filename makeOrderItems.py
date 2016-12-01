#separates the orders from the refunds and sets the values for productId, itemType and qty

from decimal import Decimal
import csv

merged = open('../clean-formattedFiles/mergedFiles/purchaseContactId.csv')
csv_merged = csv.reader(merged)

orders = open("../clean-formattedFiles/mergedFiles/SEorders.csv", 'wt')
wr_orders = csv.writer(orders, quoting=csv.QUOTE_ALL)

refunds = open("../clean-formattedFiles/mergedFiles/SErefunds.csv", 'wt')
wr_refunds = csv.writer(refunds, quoting=csv.QUOTE_ALL)

skipped = open("../clean-formattedFiles/mergedFiles/SEskipped-purchases.csv", 'wt')
wr_skipped = csv.writer(skipped, quoting=csv.QUOTE_ALL)


skipped=0
iterator=0
#productId=24 for all


def isDecimal(value):
  try:
    float(value)
    return True
  except:
    return False


for row_merged in csv_merged: #get row
  iterator+=1

  if iterator == 1: #write header to both of the new files
    wr_refunds.writerow(row_merged)
    wr_skipped.writerow(row_merged)
    #row_merged.extend(["productId","itemType","qty","payAmount"]) #adds to header but doesn't error during calcutation
    wr_orders.writerow(row_merged)

  if iterator !=1:
    if row_merged[7] == "X": #and row_merged[11] == "": #check column for refund and no products
      wr_refunds.writerow(row_merged)
    elif row_merged[7] == "N": #and row_merged[11] != "": #check column for new order and products
      #products = row_merged[11].split(" ") #not all products ordered are in Infusionsoft
      row_merged.append(24)
      row_merged.append(4)
      row_merged.append(1)
      #row_merged[33] = 24 #productId
      #row_merged[34] = 4  #itemType
      #row_merged[35] = 1  #qty
      
      if isDecimal(row_merged[13]):#prodcutPrice
        productPrice = Decimal(row_merged[13])
        productPrice = round(productPrice,2)
      else:
        productPrice = 0
        
      if isDecimal(row_merged[14]):#taxApplied
        taxApplied = Decimal(row_merged[14])
        taxApplied = round(taxApplied,2)
      else:
        taxApplied = 0
      
      if isDecimal(row_merged[15]):#shippingCharges
        shippingCharges = Decimal(row_merged[15])
        shippingCharges = round(shippingCharges,2)
      else:
        shippingCharges = 0
    
      #row_merged[36] = productPrice + taxApplied + shippingCharges #payamount
#NOT ADDING SHIPPING OR TAX
      payAmount = productPrice #+ taxApplied + shippingCharges #payamount
      row_merged.append(payAmount)
      wr_orders.writerow(row_merged)
    else:
      wr_skipped.writerow(row_merged)
      skipped+=1

print("# of Skipped Records=",skipped)

merged.close()

