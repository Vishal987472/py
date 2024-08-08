import math
a = int(input("Enter a number :"))
if a % 2 !=0:
    a *= a
    print("square is ",a)
else:
    b = math.sqrt(a)
    print("root is", b)