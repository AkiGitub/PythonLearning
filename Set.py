
#sets ---------------------------------------------------------
sets = set()
sets = {"a","b","c",1,True,2,3,3,"a"}  #1 = true

print(sets)  #{'a', 1, 2, 3, 'c', 'b'} is random answer and True is removed because it eqaul to 1
print(len(sets)) #6 

for x in sets:
    print(x)  #this is random two

if 'a' in sets:
    print('a is exist in set')  #or in not

if 'cc' not in sets:
    print('cc is not exist in set') 

#union
set1 = {'a','b','c'}
set2 = {1,2,2,3}

set3 = set1.union(set2)
set3 = set1 | set2
print(set3)  #random  {'b', 1, 'c', 2, 3, 'a'}

set1.update(set2)
print(set1) #random  {'b', 1, 'c', 2, 3, 'a'} we update the set1

#intesection 
set1 = {'a','b','c'}
set2 = {'b','a'}

set3 = set1.intersection(set2)
print(set3)  #{'b', 'a'}

set4 = set2.intersection(set1)
print(set4)  #{'b', 'a'}

set1.intersection_update(set2)
print(set1) #{'b', 'a'}

#diff
set1 = {'a','b','c'}
set2 = {'b','a'}

set3 = set1.difference(set2) # set3 = set1 - set2
print(set3) #{'c'}

set2.difference_update(set1)
print(set2)  #set() is the empty set of set2

#check is empty or not
if (set2 == set()):  #or len(set2) == 0
   print('the list is empty')

#add to list 
set2.add('a')
set2.add('b')
print(set2)  #{'a', 'b'}

#add sets
set1 = {'c','d'}
set2.update(set1)
print(set2)  #{'c', 'b', 'd', 'a'}

#add list 
list = ['list1','list2']
set2.update(list)
print(set2)  #{'a', 'd', 'b', 'c', 'list2', 'list1'}
set2.difference_update(list)
print(set2)

#add dic
dic = {'k1':'v1','k2':'v2'}
set2.update(dic)
print(set2)  #{'a', 'k1', 'd', 'k2', 'b', 'c'} #Add keys

#remove
set2.remove("k1")  #error for is not exist
print(set2) #{'c', 'a', 'd', 'b', 'k2'}
set2.discard("ddd") #there is no error 
set2.discard("k2") #{'c', 'b', 'd', 'a'}
print(set2)# 

x = set2.pop()
print(x)     # a
print(set2)  # {'d', 'c', 'b'}

#delete the list 
del set2 #Error with Access to it name 'set2' is not defined

#clear the set
set2 = {'a','b','c'}
set2.clear() #set()

#suvset
set2={'a','b','c'}
set1= {'a','b'}

print(set1.issubset(set2)); #true
print(set2.issubset(set1)); #false

#is not exist 
set3 = {'y','v'}  
print(set2.isdisjoint(set3)) #true  <=
print(set2.isdisjoint(set1)) #false {a,b}

#if exist all items set in other set
print(set2.issuperset(set1)); #true  >=

#remove dublicate
numbers = [1,1,2,3,2,4]
uniques = set(numbers)
print(uniques) #{1,2,3,4}

set1 = {x*2 for x in range(5)}
print(set1) #{0, 2, 4, 6, 8}








     










