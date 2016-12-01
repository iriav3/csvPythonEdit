#set country code to country name

import pycountry
import csv

old_format = open('../clean-formattedFiles/tempCustomerAddressProduct.csv')
csv_old_format = csv.reader(old_format)

new_format = open("../clean-formattedFiles/addresses_CName2.csv", 'wt')
wr_new_format = csv.writer(new_format, quoting=csv.QUOTE_ALL)

iterator=0
 
for row_old_format in csv_old_format: #get row
  iterator+=1
  if iterator == 1:
    wr_new_format.writerow(row_old_format)
  else:
    #check for (string)countryCode in the list and if it is then get the official name of that country
    countryCode = str(row_old_format[7])

    if len(countryCode)>3:
      if len(countryCode)==1:
        countryCode = "00"+countryCode
      if len(countryCode)==2:
        countryCode = "0"+countryCode
    validCodes = ["004","008","010","012","016","020","024","028","031","032","036","040","044","048","050","051","052","056","060","064","068","070","072","074","076","084","086","090","092","096","100","104","108","112","116","120","124","132","136","140","144","148","152","156","158","162","166","170","174","175","178","180","184","188","191","192","196","203","204","208","212","214","218","222","226","231","232","233","234","238","239","242","246","248","250","254","258","260","262","266","268","270","275","276","288","292","296","300","304","308","312","316","320","324","328","332","334","336","340","344","348","352","356","360","364","368","372","376","380","384","388","392","398","400","404","408","410","414","417","418","422","426","428","430","434","438","440","442","446","450","454","458","462","466","470","474","478","480","484","492","496","498","499","500","504","508","512","516","520","524","528","531","533","534","535","540","548","554","558","562","566","570","574","578","580","581","583","584","585","586","591","598","600","604","608","612","616","620","624","626","630","634","638","642","643","646","652","654","659","660","662","663","666","670","674","678","682","686","688","690","694","702","703","704","705","706","710","716","724","728","729","732","740","744","748","752","756","760","762","764","768","772","776","780","784","788","792","795","796","798","800","804","807","818","826","831","832","833","834","840","850","854","858","860","862","876","882","887","894"]

    if countryCode in validCodes:
      countryObj = pycountry.countries.get(numeric=countryCode)
      row_old_format[7] = countryObj.name
      print(iterator,": ",countryObj.name," == ",countryCode," == ",row_old_format[7])
    else:
      row_old_format[7] = "United States"

    wr_new_format.writerow(row_old_format)

old_format.close()

