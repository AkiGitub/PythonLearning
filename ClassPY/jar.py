class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self._size =0  

    def __str__(self):
          return self.size * '🍪'
 

    def deposit(self, n):
           self.size = n


    def withdraw(self, n):
            self.size = -1 * n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,value):
        if value<=0:
            raise ValueError

        self._capacity= value


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        newSize= self.size+value
        if newSize < 0:
             raise ValueError('jar\'s capacity is empty')

        if newSize > self.capacity:
            raise ValueError('jar\'s capacity is full')
        self._size =newSize



jj = Jar()

jj.deposit(3)

print(jj)
