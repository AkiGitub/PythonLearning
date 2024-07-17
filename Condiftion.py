
from enum import Enum

a = 2 
b = 3

if a>b:
   print('a>b')
elif a==b:
   print('q=b')
else:
   print('a<b')

#short
print("a<b") if a<b else print('a>=b')

#3 mode
a=b =10
# exp if exp else 
print('a<b') if a<b else  print('a=b') if a==b else print('noe')

if a>3 and a>4:
   print('a>4')

if a>3 or a>4:
   print('a>4')

#match 
def http_error(status):
    match status:
       case 400:
          return 'Bad request'
       case 401|402|404:
          return 'Not allowed'
       case 404:
          return "Not found"
       case 418:
          return 'I\'m teapot'
       case _: # If no case matches, <---------------
          return "something's wrong"
        
print(http_error(100)) #something's wrong
print(http_error(400)) #Bad request

#unpacking assignments
point = 12      #ValueError: Not a point
point = (10,10) #x=10 , y=10
point = (10,0)  #x=10
point = (0,10)  #y=10

match point:
   case (0,0):
      print('Origin')
   case (0,y): #bind value from piont, you do not know what is it or not important
      print(f'y={y}')
   case (x,0): 
      print(f'x={x}') 
   case (x,y):
      print(f'x={x} , y={y}')
   case _:
      raise ValueError('Not a point')
   
#attributes into variables 
class Point:
   def __init__(self,x,y):
      self.x = x
      self.y = y

def where_is(point):
   match point:
      case Point(x=0,y=0):
         print('-->orogin')
      case Point(x=0,y=y):
         print(f'y={y}')
      case Point(x=g,y=0):
         print(f'x={g}')
      case Point(x=x,y=y):
         print(f'x={x} , y={y}')
      case _:
         print("Not a point")


where_is(Point(0,0)) #-->orogin
where_is(Point(0,10)) #-->y=10

class PointArg:
      __match_args__ = ('x','y')
      def __init__(self,x,y):
         self.x = x
         self.y = y

points = PointArg(0,0) #==>something else
points = [PointArg(0,0)] #==>the origin
points = [] #==>no points
points = [PointArg(1,1)] #==>Single point 1, 1
points = [PointArg(0,1),PointArg(0,2)] #==>Two on the Y axis at 1, 2

match points:
   case []:
      print("==>no points")
   case [PointArg(0,0)]:
      print('==>the origin')
   case [PointArg(x,y)]:
       print(f"==>Single point {x}, {y}")
   case [PointArg(0,y1),PointArg(0,y2)]:
       print(f"==>Two on the Y axis at {y1}, {y2}")
   case _:
      print('==>something else')

points = PointArg(1,1) #Y=X at 1
points = PointArg(0,1) #Not on the diagonal

match points: 
   case PointArg(x,y) if x==y:
      print(f"Y=X at {x}")
   case PointArg(x,y) if x>y or x<y:
        print(f"Not on the diagonal")


class Color(Enum):
   RED = 'red'
   GREEN = 'green'
   BLUE = 'blue'

try:
  color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
  match color:
   case Color.RED:
      print('red')
   case Color.GREEN:
      print('green')
   case Color.BLUE:
      print('blue')
   case _:
      print('other')
except:
   print('error')


x, y = 50, 25
small = x if x < y else y
print(small) #25

if 'bag' > 'apple':
   print('bag')

for i in range(8):
    for j in range(0,i,2):
       print('*')




 