class TrackableList(list):
      def append(self,object): #extend
          print('added new item')
          super().append(object)

list1= TrackableList()
list1.append('zogo') #we see printed ‘added new item’

