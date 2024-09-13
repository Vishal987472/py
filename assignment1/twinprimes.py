limit = int(input("Enter a number : "))
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes(num):
    for i in range(2, num - 1):
        if check_prime(i) and check_prime(i + 2):
            print(f"({i}, {i + 2})")

twin_primes(limit)