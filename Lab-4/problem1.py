# Problem 1: Loop over a sequence

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print("Iterating over fruits list:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")