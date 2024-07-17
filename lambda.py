bozorg = lambda s:s.upper()

print(bozorg('ali'))  #ALI

def my_map(my_fun,my_iter):
    result = []
    for item in my_iter:
        new_item = my_fun(item)
        result.append(new_item)
    return result

nums = [1,2,4]
cubed = my_map(lambda x: x **2,nums)
print(cubed) #[1, 4, 16]
cubed = my_map(lambda x: x + 10,nums)
print(cubed) #[11, 12, 14]
#------------------------------------------------
modele = lambda x,y: x ** 2 + x*y
print(modele(2,2)) #8
#or
print((lambda x,y : x+y)(4,5)) #9


#------------------------------------------------
x = lambda a : a+10

print(x(5)) #15

x = lambda a,b : a*b

print(x(10,10)) #100

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfun(n):
    return lambda a : a *n

print(myfun(2)) #<function myfun.<locals>.<lambda> at 0x00000257788CDB20>

myDouble = myfun(2)
print(myDouble(10)) # 20
myTriple = myfun(3)
print(myTriple(10)) #30