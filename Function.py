def fib(n):
    result = []
    a , b = 0 , 1
    while a<n:
        result.append(a)
        a , b = b, a+b

    return result

print(fib(10)) #[0, 1, 1, 2, 3, 5, 8]

def aks_ok(prompt, retries=4, reminder = 'Please try again!'): #must be in last
    while True:
        replay = input(prompt)
        if replay in {'y','yes','ye'}:
            return True
        if replay in {'n','no','nope'}:
            return False
        retries = retries - 1
        print(retries)
        if retries < 0:
            raise ValueError(' --- invalid ---')
        
        print(reminder)

#print(aks_ok('Do you really want to quit?')) #true

#v = 0

#print(v,aks_ok(retries=56,prompt='Do you really want to quit?')) #true
#print(v)

i =5 

def f(a,L=[]):
    L.append(a)
    return L

print(f(1)) #[1]
print(f(2)) #[1,2]

def f2(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1)) #[1]
print(f2(2)) #[2]

def parrot(vol3,vol,state='satate',action='action',typed='type'):
    print('====>vol',vol,vol3)
    print('state',state)
    print('typed',typed)
    print('action',action)

parrot(vol=1,vol3=4) #not order by writed in the function
#parrot()  # missing 1 required positional argument: 'vol'
#parrot(10) # vol 10, state=state,...
#parrot(10,action='action new') #vol 10, action=action new
#parrot(110,vol=100) #got multiple values for argument 'vol'
#parrot('1','2','3') # vol =1 , state=2, action=3, type=type

def getArg(kind,*arguments):
    print(type(arguments)) #<class 'tuple'>
    for arg in arguments: #like tuple
        print(arg)

getArg("kind", "arg1","arg2","arg3") # arg1, arg2, arg3

def getKeys(kind,**keywords):
    print(type(keywords)) #<class 'dict'>

    for kw in keywords:
        print(kw, ' : ', keywords[kw]) 


getKeys(1,key1="key1",key2="key3",key3= "ley3") #key1:key1, key2:key2 ,...


#Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d): 
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion
def fib(n):
  if n<=1:
    return n
  else:
    return fib(n-1) + fib(n-2)

print(fib(7)) #13   1 1 2 3 5 8 13


def fact (n):
  if n<=1:
    return n
  else:
    return fact(n-1) * n
  
print(fact(3)) #6

def expensive(arg1,arg2,*,_cashe={}):
   if (arg1,arg2) in _cashe:
      print('in cashe')
      return _cashe[(arg1,arg2)]
   
   #cal 
   result = arg1+arg2
   _cashe[(arg1,arg2)] = result
   return result

print(expensive(1,2)) #3
print(expensive(1,2)) #in cashe
print(expensive(1,3)) #4

#intenetion 
def mult(*numbers):
   total = 0
   for num in numbers:
      total += num
      return total  #change inted to calulate properly

print('Total:',mult(1,2,3)) #1

 