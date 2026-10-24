# Problem 4: Check if character is a vowel

char = input("Enter a single character: ").strip().lower()

if len(char) != 1 or not char.isalpha():
    print("Invalid input. Please enter a single alphabetic character.")
elif char in "aeiou":
    print(f"'{char}' is a vowel.")
else:
    print(f"'{char}' is not a vowel.")