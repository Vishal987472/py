import math

def factorial(n):
    return math.factorial(n)

def permutation(n, r):
    return factorial(n) / factorial(n-r)

def combination(n, r):
    return permutation(n, r) / factorial(r)

# Test the functions
n = int(input("Enter Number of objects :"))
r = int(input("Enter Number of objects to select :"))

print(f"Number of permutations of {n} objects taken {r} at a time: {permutation(n, r)}")
print(f"Number of combinations of {n} objects taken {r} at a time: {combination(n, r)}")