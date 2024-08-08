a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print("Largest number is :", largest)