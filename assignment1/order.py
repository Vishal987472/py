a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

# Use a for loop to iterate over the list
for num in a:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# Print the even numbers
print("Even numbers:")
for num in even:
    print(num)

# Print the odd numbers
print("\nOdd numbers:")
for num in odd:
    print(num)