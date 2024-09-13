sum = 0
i =0
num = int(input("enter a number :"))
while num>0:  
    i = i + num % 10
    sum = sum + i
    i = num/10
    print(sum)