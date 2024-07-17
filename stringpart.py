

b= """
this data must be transfered to the server, and must serverd and data must solved
    this is the end of the story
"""
print(b)

print(len(b))

#access
str1 = "Hello, World"
print(str1[4]) #o
print(str1[2:4]) #ll

for x in str1:
    print(x,end=',')

#check
print('Wo' in str1) #true
print('wo' in str1) #false

#lower & upper & swap
s = "ali go to SchOOl";
print(s.lower())  #ali go to school
print(s.upper())  #ALI GO TO SCHOOL
print(s.swapcase()) #ALI GO TO sCHooL

#remove space , ...
s = "  d B  Abbd...,$d    "
print(s.strip()) #d B  Abbd...,$d
print(s.rstrip()) #  d B  Abbd...,$d
print(s.lstrip()) #d B  Abbd...,$d   #remove from left

#remove chars from fist or last  or both
print('www.examwple.comw'.strip('w')) #.examwple.com
print('d B  Abbd...,$d'.strip('d')) # B  Abbd...,$
print('d B  Abbd...,$d'.lstrip('d')) # B  Abbd...,$d do not remove sapce 

#replace  chars
print('d B  Abbd...,$d'.replace('d','$')) #B  Abb$...,$$
print('d B  Abbd...,$d'.replace('A,bb','$')) #d B  Abbd...,$d
print('d B  Abbd...,$d'.replace('Abb','$')) #B  $d...,$d

#split
s = 'ali,reza,hassan'.split(',')
print(s) #['ali', 'reza', 'hassan']

s = 'ali\n,reza,hassan'.splitlines(True) 
print(s) #['ali\n', ',reza,hassan'] keep \n 

#partition
txt = "I could eat bananas all day".partition('bananas')
print(txt) #('I could eat ', 'bananas', ' all day') 

txt = "I could eat bananas all day bananas all t".partition('bananas')
print(txt) #('I could eat ', 'bananas', ' all day bananas all t')

txt = "I could eat bananas all day bananas all t".rpartition('bananas')
print(txt) #('I could eat bananas all day ', 'bananas', ' all t')

#merge
a = 'hello '
b = 'world'

c = a+b
print(c) #hello world

#First Letter just not All words
print('heloo, ali , hassa'.capitalize()) #Heloo, ali , hassa

print('heloo, ali , hassa'.casefold()) #heloo, ali , hassa

#fill
print('ali'.center(10,'$'))#$$$ali$$$$
print('ali'.rjust(10,'$')) #$$$$$$$ali

#count is not len
print('heloo, ali , hassa'.count('a')) #3
print('heloo, ali , hassa'.count('ha')) #1
print('heloo, ali , hassa'.count('ha',1,5)) #0

#if end with 
txt = "ali want to go school. go"
print("end wit: ",txt.endswith('ool.')) #true

#expand tabs
print(txt.expandtabs(4)) 

#find / index(ValueError: substring not found)
print(txt.find('go')) #12
print(txt.find('go',20,27)) #23
print(txt.find('x')) #-1  but in index we see error

txt = "Hello, welcome to my world.e"
print(txt.rfind("e")) #27
print(txt.rfind("e")) #1


#ignore other english chars---------------------------------------------------------
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="ignore")) #b'My name is Stle'

#expalin other char
#b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(txt.encode(encoding="ascii",errors="namereplace"))

#b'My name is St?le'
print(txt.encode(encoding="ascii",errors="replace"))

#identififier
a = "MyFolder"
b = "Demo002"
c = "2bring"   #start with 2
d = "my demo"  #has space
print(a.isidentifier())  #true
print(b.isidentifier())  #true
print(c.isidentifier())  #false
print(d.isidentifier())  #false
print('#esfd'.isidentifier()) #false

#check for space as whole
print("   ".isspace()) #true
print("  d ".isspace()) #false

#fill with zero
print('ali'.zfill(10))

#Make trans ----------------------------------------
txt = "hi samar!"
x = "msar"
y = "BAKR"
mytable = str.maketrans(x,y)
print(txt.translate(mytable))

#pritable 
txt = "Hello!\nAre you #1?"
print(txt.isprintable()) #false bc of the \n in the text

#all  letters are CAP
print("LIFE IS STRANGe".isupper()) #false

#================================================join Dic,tuple
dic = {"name":"ali","age":24,"price":100}
tup = ('1','2','3')
mySep = "_SEP_"
print(mySep.join(dic)) #name_SEP_age_SEP_price
print(mySep.join(tup)) #1_SEP_2_SEP_3

#min and max -------------------------------------------
print(min('DaccdTA')) # A
print(max('DaccdTA')) # d

#Reversed String -----------------------------------------
str1 = '0123456789'
print(str1[::]) #0123456789
print(str1[::-1]) #fedcba
print(str1[::-2])  #fdb (0 2 4)
print(str1[::-3])  #fc  (0 3)
print(str1[::-4])  #fb  (4)

#ignore escape 
String1 = r"This is \110\145\154\154\157"
print(String1) #This is \110\145\154\154\157