# observing the behaviour of dynamic array 
import sys
# l = []
# for i in range(100):
#     print(i,sys.getsizeof(l))
#     l.append(i)

# creating the own list using c data types importing ctypes
import ctypes

class ownList:
    def __init__(self):
        self.size = 1 # how many items can be stored
        self.n = 0 # how many items are included right now 
        self.A = self.create_array(self.size)

    def __len__(self):
        return self.n

    # def __append__(self):


    def create_array(self,capacity):
        # creating  a C type array(static,referential) with size capacity
        return (capacity * ctypes.py_object)()



l = ownList()
print(l.__len__())