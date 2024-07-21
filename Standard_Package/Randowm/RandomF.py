import random
import string

print(random.random())# (0,1) 0.549631968571194
print(random.randint(1,10))#  3
print(random.choice([1,2,3,4]))#  4
print(random.choices([1,2,3,5,4],k=2))#  two randow values [1,3]
#for password
print(random.choices("abcdefghkn",k=4))#  ['k', 'e', 'd', 'd']
print("".join(random.choices("abcdefghkn",k=4)))# nhck
print(",".join(random.choices("abcdefghkn",k=4)))# g,d,b,d
#all letters
print("".join(random.choices(string.ascii_letters + string.digits,k=4)))# Y2ck 

#random order list
numbers = [1,2,3,4]
random.shuffle(numbers)
print(numbers) #[2, 4, 1, 3]



