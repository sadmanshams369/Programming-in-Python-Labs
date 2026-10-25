# Lab 02 - Problem 3: Basic Input/Output and Variable Exploration

# 1. Variable Assignment (created automatically upon first assignment)
x = 5
name = "John"
print("Initial x:", x, "| Type:", type(x))
print("Initial name:", name, "| Type:", type(name))

# 2. Dynamic Typing (reassigning a variable to a different type)
x = "Now I am a string"
print("Reassigned x:", x, "| Type:", type(x))

# 3. User Input and Output Variations
username = input("\nEnter your username: ")

# Formatted outputs
print("Username is:", username)
print("Username is: " + username)
print(f"Username is: {username} (using f-string)")

# Checking the type returned by input()
print("Type of input value:", type(username))