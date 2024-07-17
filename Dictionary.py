dic= {"name":'ali',"age":12,"age":123}
#{'name': 'ali', 'age': 123}

for x in dic:
    print('=================',x) #name , age
     
#access
print(dic['age'], dic['name']) #123 ali
print(dic.get('age'), dic.get('name'))#12 ali

#keys / Values
print(dic.keys())  #dict_keys(['name', 'age'])
print(dic.values())#dict_values(['ali', 12])

#new item  & change value
dic['grade'] = 20
dic['name'] = 'akbar'
print(dic) #{'name': 'akbar', 'age': 12, 'grade': 20}

#convert to list [(key,value),(..)]
print(dic.items()) #dict_items([('name', 'akbar'), ('age', 12), ('grade', 20)])

#Check is in the dic
if 'name' in dic:
    print('vicotry')

#update add/change
dic.update({'name':'zogo'})
print(dic.values()) #dict_values(['zogo', 12, 20])

#pop
x = dic.pop('name') 
print(x)#zogo
print(dic.keys()) #dict_keys(['age', 'grade'])

dic2 = dic.copy()
dic.clear() #or del dic 
print(dic.keys(),dic2.keys()) #dict_keys([]) dict_keys(['age', 'grade'])

#create dic with tuple
x = ('key1','key2','key3')
y = 20 
dic = dict.fromkeys(x,y+2)
print(dic) #{'key1': 20, 'key2': 20, 'key3': 20}

#for check the values frrom the dictionary
for x in dic.values():
    print(x) 

for x,y in dic.items(): #key,value
    print(x,y)#  key1 20 ,...

#Nested Dictionary------------------------------------
myfamily = {
    'child1':{
      "name":"ali",
      "age":12
    },
       'child2':{
      "name":"mona",
      "age":45
    },
    'child3':{
      "name":"reza",
      "age":23
    },
}

#access nested:
print(myfamily['child1']['name']) #ali

#for
for x,obj in myfamily.items():
    print(x) #child1,2,3

    for y in obj:
        print(y +":",obj[y]) #
         #child 1
         #name: ali
         #age: 23

#del specefic items
users = {"Hans":"active","Dani":"inactive","zogo":"active"}

for user,status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users) #{'Hans': 'active', 'zogo': 'active'}

#or create another dictionary
users = {"Hans":"active","Dani":"inactive","zogo":"active"}
active_users = {}
for user,status in users.items():
    if status == 'inactive':
        active_users[user] = status
    
print(active_users) #{'Dani': 'inactive'}

#dic as argument
def fun3(args):
    args['a'] = 'new-value'
    args['b'] = args['b'] +1

dic = {'a':'zogo','b':99}
fun3(dic)
print(dic) #{'a': 'new-value', 'b': 100}

#another add value 
point2 = dict(x=1,y=2)
print(point2) #{'x': 1, 'y': 2}

#expresion in the dictionary
values = {x:x*2 for x in range(5)}
print(values) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


#unpacking -----------------------------------------
dic1 = {'x':1}
dic2 = {'x':10,'y':20}
combinedDic = {**dic1,**dic2,"z":1} #{'x': 10, 'y': 20, 'z': 1}
print(combinedDic)


#sorted program in dictionary (find char count)

import pprint 
sentence = "This is a common interview question"
print('_____________________________________________')
char_freq = {}

for char in sentence:
    if char in char_freq:
       continue
    else:
        char_freq[char]= sentence.count(char)



sorted=sorted(char_freq.items(), key=lambda kv:kv[1],reverse=True)
pprint.pprint(sorted,width=10)
print(sorted[0]) #('i', 5)