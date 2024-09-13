import numpy as np
# n1 = np.array([(1,2,3)])
# n2 = np.array([(4,5,6)])
# print(np.vstack((n1,n2)))
# print(np.hstack((n1,n2)))
# print(np.column_stack((n1,n2)))

arr = np.array([4,5,6,7])
filter_arr = []
for element in arr:
    if element > 5:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

from numpy import random
a = random.randint(1000)
print(a)
b = random.rand(3,4)
print(b)
c = random.choice(5)
print(c)