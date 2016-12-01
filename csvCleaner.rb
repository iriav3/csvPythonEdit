#This script is for cleaning the data from a given CSV file.
#It will remove all instances of \N within each line of a file
#and new lines inside a field/quotes 
#thereby placeing it all on one line in the file so I can be read as a single row.

#The criteria of what goodStartChars()=true or goodLastChar()=ture or goodLastChar2()=ture
#may change depending on the file.

def removeNulls(oldLine)
  newLine = oldLine.gsub!('\\N','')
  if newLine
    return newLine
  else
    return oldLine
  end
end


def removeLineBreak(line)
  if line.nil?
    return ""
  else
    newline = line.gsub!("\n"," ")
    return newline
  end
end


def goodStartChars(line)
  if line.nil?
    return false 
  else
    startChars = line[0,3]
    if startChars == "\"se" # "se is the start for every row
      return true
    else
      return false
    end
  end
end


def goodLastChar(line)
  if line.nil?
    return false
  else
    lastChar = line[-2,1]
    if lastChar == "\"" or lastChar == "," #last char before newline char is a " or ,
      return true
    else
      return false
    end
  end
end


def goodLastChar2(line)
  if line.nil? or line.length<5 #whole row must be larger than 5 char
    return false
  else
    lastChar2 = line[-3,2]
    if lastChar2[-2,1]!="," and lastChar2[-1,1] == "\"" #last 2 char before newline char ,"
      return true
    else
      return false
    end
  end
end


def mergeString(line1,line2)
  if !line1.nil? and !line2.nil?
    line1 << line2
    return line1
  elsif line1.nil? 
    print "L2=",line2
    return line2
  elsif line2.nil? 
    print "L1=",line1
    return line1
  end
end


previousLine=""
mergeLine=""
rowCount=0
badRowCount=0
goodMergeRow=0


File.open("../superCleanCustomer.csv","w") do |output|
  File.readlines("../../SE_20160622_pmcCustomer.csv").each do |inputLine|
    rowCount+=1
    newLine = removeNulls(inputLine)
    if rowCount==1
      output.puts newLine
    else
      if goodLastChar(newLine) and goodStartChars(newLine) and newLine.count("\"")%2 == 0
        output.puts newLine
        previousLine = ""
      else
        badRowCount+=1
        if goodStartChars(newLine)
           previousLine = newLine
        else
          previousLine = removeLineBreak(previousLine)
          mergeLine = mergeString(previousLine,newLine) 
          print "merged lines = ",mergeLine,"\n"
          if goodLastChar2(mergeLine) and goodStartChars(mergeLine) and mergeLine.count("\"")%2 == 0
            goodMergeRow+=1
            output.puts mergeLine
          end
        end
      end
    end
  end
end


print "badRows/totalRows => ",badRowCount,"/",rowCount," => ",(badRowCount.to_f/rowCount.to_f*100).round(2),"%","\n"
print "good rows on new file => ",rowCount-(badRowCount-goodMergeRow),"\n"

