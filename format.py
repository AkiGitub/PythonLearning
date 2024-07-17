
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name)) #His name is John. John is 36 years old.


txt = "my name is {name} with age {age}".format(name='akbar',age=12)
txt = "my name is {0} with age {1}".format('akbar',12)
txt = "my name is {} with age {}".format('akbar',12)
print(txt) #my name is akbar with age 12

age = 36
print(f"the age is {age}") #the age is 36
print(f"the age is {age + 2}") #the age is 38

price = 59
print(f"the price is {price:.2f}") #the price is 59.00

#Escape Chars
str1 = "we ara ling in the \"KOLO\" "
print(str1) #we ara ling in the "KOLO"

#\\
str1 = "x \\ y = 30"
print(str1) #x \ y = 30

#\n
str1 = "Hello\n Ali"
print(str1) #two lines

#\t
str1 = "Hello\t Ali"
print(str1) #Hello    Ali

#\b
str1 = "AliR\bR"
print(str1) #AliR

#Hex & Oct
txt = "\65\66\67" 
print(txt)

txt = "\x65\x66\x67" 
print(txt) #efg


print('Comapnt12'.isalnum()) #true (space)!#%&? not accepted
print('Comapany123%%'.isascii()) #true
print('Comapany123\n%^'.isascii()) #true

#is decimal
print('123.2'.isdecimal())#false
print('123'.isdecimal())#ture
print('123'.isdigit())#false

#format of {} .0
print("your score is {:%}".format(0.25)) #your score is 25.000000%
print("your score is {:.0%}".format(0.25)) #your score is 25%

#hex or oct
print("Hex {0:X} / {0:x}".format(255)) # FF / ff

#binary to decimal
print("{:d}".format(0b10101)) # 21 (16+5=21)

#add + to positive number
print("{:+} and {:+} ".format(-3,7)) #-3 and +7

#Add space format
print("ali{:=5}go".format(-5)) #ali-   5go

#money sepeartor
print('{:,}'.format(13000000))  #13,000,000

#binary
print("binary of {0} is {0:b}".format(5)) #binary of 5 is 101










