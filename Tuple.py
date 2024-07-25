#readonly list !add,!change

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

#access  [m:n]= [m,0-n-1] , [:]
print(thistuple[:]) #('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple[1]) #banaan
print(thistuple[2:4]) #('cherry', 'apple') [2:4-1]
print(thistuple[:3]) #('apple', 'banana', 'cherry') (n-1)
print(thistuple[3:]) #('apple', 'cherry')
print(thistuple[-3:-1]) #

#Add to Tuple with List-----------------------------
thistuple = ("apple", "banana", "cherry")
list1 = list(thistuple)
list1.append("oragne")
thistuple= tuple(list1)
print("Added to list: ",thistuple)

#add another tuple-----------------------------------
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y



thistuple= tuple(list1)#('apple', 'banana', 'cherry', 'oragne')
print("Added tuple to list: ",thistuple) 

#remove one item by list-----------------------------
y = list(thistuple)
y.remove('oragne')
thistuple = tuple(y) # ('apple', 'banana', 'cherry')
print("remove an item: ",thistuple)

#del the tuple  -------------------------------------
del thistuple

ftuits = ('apple', 'banana', 'cherry')
(a1,a2,a3) = ftuits
print(a1,a2,a3) #apple banana cherry

#count (find)----------------------------------------
t = ('1','ff','11','33','f1')
c = t.count('1') #1
c2 = t.count('') #0
inx = t.index('f1') #4 #can be error if not found
print(c,c2,inx)

#for
for x in t:
    print(x)

print('other way')
for i in range(len(t)):
    print(t[i])

i=0
while i<len(t):
    print(f"Upper case {t[i].upper()}:")
    i=i+1

#tuples join ----------------------------------
t1 = ('a','b','c')
t2 = (1,2,3)

t = t1 + t2 #('a', 'b', 'c', 1, 2, 3)
print(t)

t = t2 * 2 #two times not value mutiply by 2
print(t) #(1, 2, 3, 1, 2, 3)

#combine tuple
thistuple = (1,2) + (1,3)

#mult 
thistuple = (1,2) *3 #(1,2,1,2,1,2)

#convert list to tuple
points = tuple([1,2])
letters = tuple("abcds") #('a','b', ..)

x= 1
y=4
roundedValue = int((round(int(x) / int(y),2)) *100)
print(roundedValue)