# observing the behaviour of dynamic array 
import sys
l = []
for i in range(100):
    print(i,sys.getsizeof(l))
    l.append(i)