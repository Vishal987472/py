a = [2,4,3,5,2,4,5,8,2,3]

count = 0
for i in set(a):
    count = a.count(i)
    print(i,end=" ")
    print(count)



# collection method

# from collections import Counter

# a = [2,4,3,5,2,4,5,1,2,3]
# counts = Counter(a)

# for key, value in counts.items():
#     print(key, end=" ")
#     print(value)