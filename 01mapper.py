import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 4) : 
    Country_Name,Country_Code,Year,Value = datalist
    
    # print intermediate key-value pairs to standard output
    print(Country_Name,"\t",1)    
    