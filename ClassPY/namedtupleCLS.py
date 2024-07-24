from collections import namedtuple

point = namedtuple("Point",['x','y'])
p1 = point(x=1,y=1)
p2 = point(x=2,y=1)

print(p1 < p2) 
print(p1[0] + p1[1])  #1+1

x, y = p1
print(x,y) #1 1
print(p2.x,p2.y) # 2 1