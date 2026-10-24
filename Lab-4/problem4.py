# Problem 4: Sum of all primes below 1000

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_sum = sum(n for n in range(2, 1000) if is_prime(n))

print(f"The sum of all primes below 1000 is: {prime_sum}")