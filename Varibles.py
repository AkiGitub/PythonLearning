import random
import package.subPackage1.config as config,mod

from sys import getsizeof


# Variables 
ix = 12
gx = 14
ifl = 1.2

def GlobalFun():
    global gx #gx is changed in this funtion 
    gx= 3     #without the global gx differ from main gx 

print("global var",gx) #global var 14 not 3

def myfunc():
  global xr
  xr = "fantastic"

myfunc()
 
print("Python is " + xr)  #Python is fantastic

# boolean ------------
b1 = bool('a')
b2 = bool(12)
print(b1,b2)
b3 = bool(False)
b4 = bool(None)
b5 = bool("")  #false
b6 = bool(())  #false
b7 = bool([])  #false
b8 = bool({})  #flase

#multiple values
x,y,z = 10,20,30

print(b3,b4,b5,b6,b7,b8)
#instance
print(isinstance(1,int))  #true 
print(isinstance(1.2,int))  #false
print(isinstance(1.2,str))  #false

#casting
print(int('1234')) # invalid literal for int() with base 10: '1234.4'
print(float('123.4')) # 123.4

print(random.randrange(1,10))  # 2 for example

#get type
print(type(10))  #int

#HEX
a = 0x65
print(a) #101  65 = 01100101 = 101

#// and /
print((10 / 2))   # 5.0
print((10 // 2))  # 5

#problem of localization ------------------------------------
squares = [] 
for x in range(5):
    squares.append(lambda: x**2)

#This happens because x is not local to the lambdas, but is defined in the outer scope, and it is accessed when the lambda is called — not when it is defined. At the end of the loop, the value of x is 4, so all the functions now return 4**2, i.e. 16. You can also verify this by changing the value of x and see how the results of the lambdas change:
print(squares[1](), squares[2]()) #16  16
   
#sovle
squares = []
for x in range(5):
   squares.append(lambda n=x: n**2)

print(squares[2](),squares[3]()) #4,6

#access to module
print(config.x)#100


#nonlocal -----------------------------

def myfun():
   x = 100
   def funinside():
      x=200
  
   funinside()
   return x

print(myfun()) #100


def myfun():
   x = 100
   def funinside():
    nonlocal x
    x = 200
  
   funinside()
   return x

print(myfun()) #200

z = 11 
x2 = 11

if z is x2:
   print('the same object')

values = (x * 2 for x in range(100000)) #200
print(getsizeof(values))

values = [x * 2 for x in range(100000)] #800984
print(getsizeof(values))