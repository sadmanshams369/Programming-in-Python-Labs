# Problem 1: Swap the values of two variables

a = input("Enter first value (a): ")
b = input("Enter second value (b): ")

print(f"Before swapping: a = {a}, b = {b}")

# Pythonic tuple unpacking swap
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")