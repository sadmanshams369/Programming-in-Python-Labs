# Problem 5: Fibonacci numbers below N

limit = int(input("Enter upper limit N: "))

a, b = 0, 1
fib_sequence = []

while a < limit:
    fib_sequence.append(a)
    a, b = b, a + b

print(f"Fibonacci numbers below {limit}: {fib_sequence}")