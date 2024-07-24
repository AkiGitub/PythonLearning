
 # bundle up values in a class instance: other way of sending dic to fun
from typing import Any

#------------------------------------------------------
#instance 
class Namesapce:
      def __init__(self,/,**args):
            for key,value in args.items():
                  setattr(self,key,value)

def fun4(args):
      args.a = 'new value'
      args.b = args.b + 1

args = Namesapce(a='new-value',b=12)                  
fun4(args)
print(vars(args)) #{'a': 'new value', 'b': 13}

#inhertance ----------------------------------------------------
class Person:
      def __init__(self,id,name):
           self.id = id
           self.name =name 
      
      def printData(self):
            print(self.id,': ',self.name)
      
class Student(Person):
      def __init__(self, id, name,className):
            super().__init__(id+1, name)
            self.className = className

stu = Student(1,'zogo','102')
stu.printData()




#You have two choices: you can use nested scopes or you can use callable objects. 
# For example, suppose you wanted to define linear(a,b) which returns a function f(x) that 
# computes the value a*x+b. Using nested scopes:
class Linear:
      def __init__(self,a,b):
            self.a, self.b = a ,b 
      
      def __call__(self, x):
            return self.a * x + self.b 

taxes = Linear(1,2)
print(taxes(1))#3


class counter:
      value = 0

      def set(self,x):
            self.value = x

      def up(self):
            self.value = self.value + 1
      
      def down(self):
            self.value = self.value - 1

count = counter()
inc , dec , reset = count.up,count.down,count.set
inc()
print(count.value)


#Iterators---------------------------------------------------
#An iterator is an object that contains a countable number of values.
t = ('t1','t2','t3')
myit = iter(t)

print(next(myit)) #t1
print(next(myit)) #t1

stri = 'zogo'
myit = iter(stri)

print(next(myit)) #t1
print(next(myit)) #t1
print(next(myit)) #t1
print(next(myit)) #t1
#print(next(myit)) #t1 StopIteration Error

class myNumber:
      def __iter__(self) :
            self.a =1 
            return self
      
      def __next__(self):
            x= self.a
            self.a +=1
            return x
      
myclass = myNumber()
myit = iter(myclass)

print('first',next(myit)) #first 1
print(next(myit)) # 2
#infinit

#StopIteration
#To prevent the iteration from going on forever,
class myNumbers:
      def __iter__(self):
            self.a = 1
            return self
      
      def __next__(self):
            if self.a<=5:
                  x= self.a
                  self.a +=1
                  return x
            else:
                  raise StopIteration

myclass = myNumbers()
myiter = iter(myclass)

for x in myiter:
      print(x, end=' , ') #1 , 2 , 3 , 4 , 5 ,

#while x in myiter:
#       print(x, end=' , ')

#Polymorphism
class Car: 
      def __init__(self,brand,model):
            self.band = brand
            self.model = model
      
      def move(self):
            print('Drive',',')

class Boat():
      def __init__(self,brand,model):
            self.band = brand
            self.model = model

      def move(self):
            print('Sail',end='#')

car1 = Car("Fors","Nus1")
boat1 = Boat('Ivo','M2')

for x in (car1,boat1):
      x.move()  # Drive, in next line Sail #

#Polymorphism & inheritance --------------------------------
class Vehicle:
      def __init__(self,brand,name):
            self.brand = brand
            self.name= name
      
      def move(self):
            print('move')
      
class car(Vehicle):
      pass

class Boat(Vehicle):
      def move(self):
            print('boat')


car1 = car('mecedes','m300')
boat = Boat('zedi','ggd1')
print()
for x in (car1,boat):
      x.move() #move boat

             
#class attribute --------------------------------
class Point:
      default_color = 'red'

      def __init__(self,x):
           self.x = x

p1 = Point(2)
p1.default_color= 'Yellow'

p2 = Point(2)
p2.default_color= 'Green'

print(p1.default_color)  #Yellow
print(p2.default_color)  #Green
print(Point.default_color)  #red

#decrator --------------------------------
class Point2:
      def __init__(self,x,y):
            self.x = x
            self.y = y

      def __add__(self,other):
           return Point2(self.x + other.x,self.y+other.y)

      def __eq__(self, other):
            return self.x == other.x and self.y == other.y
      
      def __gt__(self,other):
           return self.x> other.x and self.y > other.y
      
      @classmethod
      def zero(cls):
           return cls(0,0)
       
      def draw(self):
            print('==>',self.x,self.y)

#without the @classmethod, we cannot access to it in line
#like static method
p = Point2.zero()
p.draw()
print(p.__str__) #get name of the class

obj1 = Point2(1,2)
obj2 = Point2(1,2)
print(obj1 == obj2) #true

obj1 = Point2(5,5)
obj2 = Point2(3,2)
print(obj1 > obj2) #true

added = obj1 + obj2
print(added.x , added.y)

#dic imp in the class
class TagCloud:
      def __init__(self):
            self.__tags = {}
      
      def add(self,tag):
            self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0)+1
      
      #for [] for access to item, EX: cloud["key"]
      def __getitem__(self,tag):
            return self.__tags.get(tag.lower(),0)
      
      #for set value to the dic, cloud["key"] = count
      def __setitem__(self,tag,count):
            self.__tags[tag.lower()] = count
      
      def __len__(self):
            return len(self.__tags)
      
      #for for loop
      def __iter__(self):
            iter(self.__tags)

cloud=TagCloud()

cloud["Python"] = 10
cloud.add('Python')
cloud.add('python')
cloud.add('Python')
cloud.add('Xogo')

print("Count: ",len(cloud))  #1
print(cloud["Python"])       #13

# for key,value in cloud.__tags.items():
#       print(key,value) #python 13, xogo 1


#property ----------------------
class Product:
      def __init__(self,price):
            self.__price = price
      
      def get_Price(self):
            return self.__price
      
      def set_price(self,value):
            if value <0:
                  raise TypeError('Price > 0')
            self.__price=value

p = Product(-1)


class Product:
      def __init__(self,price):
            self.price = price
      
      #@classmethod or
      @property
      def price(self):
            return self.__price
      
      @price.setter
      def price(self,value):
            if value <0:
                  raise TypeError('Price > 0')
            self.__price=value
      

p = Product(-10)
print(p.price) #10


#inheritance

class A:
    def fun(self):
        return '1+1'
class B:
    def fun(self):
        return '2+2'

class C(A,B):
     pass


c = C()
print(c.fun())
         


