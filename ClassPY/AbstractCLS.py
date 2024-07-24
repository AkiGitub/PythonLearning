
from abc import ABC, abstractmethod

class InvalidOperatorError(Exception):
      pass

class Stream(ABC):
      def __init__(self):
           self.opened = True
      
      def open(self):
        if self.opened: #already opened 
           raise InvalidOperatorError("Already opened")
        self.opened= True
     
      def open(self):
        if not self.opened: #already opened 
           raise InvalidOperatorError("is not opened")
        self.opened= False
     
      @abstractmethod  
      def read(self):
         pass

class FileStream(Stream):
    def read(self): #must 
       print("Read file operation")

class NetStream(Stream):
    def read(self): #mustbe
       print("Read Net operation")

p1 = NetStream()
p2 = FileStream()

p1.open()
p1.read()

class UIControl(ABC):
      @abstractmethod
      def draw(self):
        pass

class TextBox(UIControl):
      def draw(self):
           print('Textbox')

class ComboBox(UIControl):
      def draw(self):
          print('ComboBox') 
          
def draw(controls):
    for clr in controls:
        clr.draw()

textbox = TextBox()
combo = ComboBox()
draw([combo,textbox]) #or duck type [fun1(),fun2()]



