a = [1,2,3,4,5,6,7,8,9,10]
b = int(input('Enter a number from 1 to 10 :'))
exist = False
for x in a:
    if x == b:
        exist = True
if exist:
    print("The number ",b,"exist in the list")
else:
    print("The number does not exist in the list")