# Problem 3: Exponentiation (base ^ exponent)

base = float(input("Enter the base: "))
exp = int(input("Enter the exponent (integer): "))

result = 1.0
positive_exp = abs(exp)

for _ in range(positive_exp):
    result *= base

if exp < 0:
    result = 1.0 / result

print(f"{base}^{exp} = {result}")