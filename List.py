from operator import itemgetter, attrgetter

list1 = [1,4,3,6,7,7]
print(list1)

#lisr based on ranged 
listRange = list(range(0,10,2))
print(">>>>>list based on range:",listRange) # [0, 2, 4, 6, 8]

#sum of the list 
print(sum(listRange))  #20

#access
print(list[1]) #2
print(list[1:3]) #4,3  [1:n-1]

#for 
for x in list1:
    print(x) #1,2,3

#len 
for i in  range(len(list1)):
    print(f" value {i} is {list1[i]}")
     
#append
list1 = []

for x in range(4):
    list1.append(x**2)
print(list1)

#comprehension --------------------------------------------
fruits =["apple", "banana", "cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist) #['apple', 'banana', 'mango']
#is equal to 

newlist = [x for x in fruits]
print(newlist) #['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if 'a' in x]
print(newlist) #['apple', 'banana', 'mango']

list1 = [1,3,4,6,7]
list2 = [x for x in list1 if x>=4]
print(list2) #[4, 6, 7]
list2 = [x*2 for x in list1] #first write for x in list then write expresion x
print(list2) #[2, 6, 8, 12, 14]

#range 
list1= [x for x in range(5)]
print(list1) #[0, 1, 2, 3, 4]
list1= [x**2 for x in range(5) if x<3] #
print('power of 2 for list--------->', list1) #[0, 1, 2, 3]
list1 = [0 for x in range(5)]
print(list) #[0, 0, 0, 0, 0]

newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
newlist = [x if x!="banana" else 'orange' for x in fruits] #change banana in list
print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']

#sort
list1 = ['aa','bb','bt','bz','ba']
list1.sort()
print(list1) #['aa', 'ba', 'bb', 'bt', 'bz']

list1 = [2,2,-1,300,3,4,1]
list1.sort(reverse=True)
print(list)  #[300, 4, 3, 2, 2, 1, -1]

#sort based on the function & key -------------------------------------------
def funSort(n):
    return abs(n-50)

list1 = [100,50,300,-1,5]
list1.sort(key=funSort)
print(list)

def funBaselen(e):
    return len(e)

cars = ['ford','Mitsubishi',"BW",'VM']

cars.sort(key=funBaselen)  #['BW', 'VM', 'ford', 'Mitsubishi']

#sort base on not sensetive to the words
list1 = ['AA',"a",'BBB','bb','aaceda']
list1.sort(key=str.casefold)   #['a', 'AA', 'aaceda', 'bb', 'BBB']
print(list1)
list1.sort() #['AA', 'BBB', 'a', 'aaceda', 'bb']
print(list1) 

#sort base on field
students = [
    ('ali',12,'m'),
    ('fati',45,'w'),
    ('mona',54,'w'),
    ('reza',23,'m'),
]
students.sort(key=lambda student:student[1]) #sort by age
print(students) #('ali', 12, 'm'), ('reza', 23, 'm'), ('fati', 45, 'w'), ('mona', 54, 'w')]
#or
students.sort(key=itemgetter(1))
print('itemgetter: ',students)

#bassed on first then second(gender)
students.sort(key=itemgetter(1,2))
print('itemgetter1,2: ',students)

students.sort(key=lambda student:student[2]) #sort by gender
print(students) #[('ali', 12, 'm'), ('reza', 23, 'm'), ('fati', 45, 'w'), ('mona', 54, 'w')]

#sort based on class field
class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    
    #without this we cannot print the class in output
    def __repr__(self):  #for represent or print the class
        return repr((self.name,self.grade,self.age)
        )
        
obj_student = [
    Student('ali',12,45),
    Student('mona',12,34),
    Student('Hassan',19,55),
    Student('zogo',20,22)
]

obj_student.sort(key= lambda student:student.age)
print(obj_student) #[('Hassan', 20, 22), ('ali', 12, 34), ('mona', 12, 45), ('zogo', 10, 55)]
#or
obj_student.sort(key=attrgetter('age'))
print(obj_student)
#two field sorting
obj_student.sort(key=attrgetter('grade','age'))
print(obj_student) #[('mona', 12, 34), ('ali', 12, 45), ('Hassan', 19, 55), ('zogo', 20, 22)]

#mosh 
zeros = [0] * 5
print(zeros)#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lettes = ['a','b','c']
combined = zeros + lettes
print(combined)

numbers = list(range(10))
print(numbers[::-1]) #[9,8,7,...]
print(numbers[::-2]) #[9,8,7,...]
print(numbers[::2])  #[0, 2, 4, 6, 8]
print(numbers[::3])  #[0, 3, 6, 9]

first, second , *other = numbers
print(first,second)
print(other)

#for tuple 
for num in enumerate(numbers):
    print(num ,end=' ') #(0, 0) (1, 1) (2, 2) (3, 3) ...
    print(num[0],num[1]) #0 0  1 1 2 2  access to the index , value

#othe implemation (unpacking)
for index,item in enumerate(numbers):
    print(index, item,end=' ')
print()
#map ------------------------
items = [
    ("p1",10),
    ("p2",11),
    ("p2",13),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices) #[10, 11, 13]

x= map(lambda item:item[1],items)
for item in x:
    print(item) #10 11 13

#or 
prices =list(map(lambda item:item[1],items))
print(prices) #[10 11 13] 
prices = [item[1] for item in items] #[10 11 13] 
print(prices)

#filter ----------------------------------------------
filterdList = list(filter(lambda item:item[1]>10,items))
print(filterdList) #[('p2', 11), ('p2', 13)]
#or 
filtedList1 = [item[1] for item in items if item[1]>10] 
filtedList2 = [item for item in items if item[1]>10] 
print(filtedList1) #[11,13]
print(filtedList2) #[('p2', 11), ('p2', 13)]

#zip----------------------------------------------
list1= [10,20,30]
list2 = [1,2,3]

list3= list(zip('ab',list1,list2))
print(list3) #[(10, 1), (20, 2), (30, 3)]

list3= list(zip('abcd',list1,list2))
print(list3) #[(10, 1), (20, 2), (30, 3)]

#unpacking advanced------------------------
values = [*range(5)]
print(values) #[0, 1, 2, 3, 4]

values = [*range(3),*"aki"]
print(values) #[0, 1, 2, 'a', 'k', 'i']

listMonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


listMonths.index('Decembers')