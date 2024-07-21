
import array as arr
#import changed
#(must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
a = arr.array('i', [1, 2, 3])
print(a)

#access---------------------------------
print(a[1]) #2

#for -----------------------------------
for i in range(0,3):
    print(a[i], end = " ")  # 1 2 3

#insert --------------------------------
a.insert(1,444)
print(a)  #array('i', [1, 444, 2, 3])

#append --------------------------------
a.append(34)
a.append(34)
print(a)  #array('i', [1, 444, 2, 3, 34])

#pop & remove ---------------------------
x = a.pop() # = a.remove(len(a)-1)
print(x,',', a) #34 , array('i', [1, 444, 2, 34])
x = a.pop(0)  #remove first item 
print(x,',', a) #1 ,array('i', [444, 2, 3, 34])
print((len(a)-1)) #3

#remove the existed item -------------------
a.remove(34) #remoe by find 
print(a)

#slicing --------------------------------------
print(a[:]) #array('i', [444, 2, 3])
print(a[0:2]) #array('i', [444, 2])

#searching & count ------------------------------------
print(a.index(2))# the frist index of 2 = 1
print(a.count(2))# number of 2 = 1

#update ---------------------------------------
a[1] = 34
print(a) #array('i', [444, 34, 3])

#reverse ---------------------------------------
a.reverse()
print(a) #array('i', [3, 34, 444])

#Extend ---------------------------------------
a.extend([1,2,3])
print(a) #array('i', [3, 34, 444, 1, 2, 3])




