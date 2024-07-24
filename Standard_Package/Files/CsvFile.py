from collections import namedtuple
import csv
import os 

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

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
for emp in map(EmployeeRecord._make, csv.reader(open(dir_path+"\\employees.csv"))):
     print(emp.name, emp.title)