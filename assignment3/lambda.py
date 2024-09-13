# max = lambda a,b: a if(a<b) else b
# print(max(2,5))

#map function

# num = [1,2,23,45]
# def sum(a):
#     return a + a

# added_num = map(sum, num)
# result = list(added_num)
# print(result)


# reduce function

import functools
num = [2,5,6,4]
num2 = [5,4,6,8]
def mul(a,b):
    return a + b
ans = functools.reduce(mul, num2)
print(ans)

#shape fucntion

# import numpy as np
# arr = np.array([[1,2,3],[6,5,4,7]])
# shape_arr= arr.shape((3,2))
# print(shape_arr)