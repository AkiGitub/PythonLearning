import csv 

# with open(r"d:\temp\dataFile.csv",'w') as file:
#      writer = csv.writer(file)
#      Header = ["name","family","age"]
#      writer.writerow(Header)
#      values = ["ali",'Reza',23]
#      writer.writerow(values)

with open(r"d:\temp\dataFile.csv") as file:
     reader = csv.reader(file)
     print(list(reader)) #pointer of the file in last then we can access the file again

     for row in reader:
          print(row)