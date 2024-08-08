# Get the input from the user
num = int(input("Enter a number: "))

# Initialize the factorial variable to 1
factorial = 1

# Initialize the counter variable to 1
i = 1

# Use a while loop to calculate the factorial
while i <= num:
    factorial *= i
    i += 1

# Print the result
print("The factorial of", num, "is", factorial)