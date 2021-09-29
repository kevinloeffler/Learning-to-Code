import random

# What if...

yes = True
no = False

if yes:
    print("Yay")

if no:
    print("Nope")


# Comparisons: > < ==

a = 5
b = 3

if a > b:
    print("Bigger")


# Nespresso, what else

if a < b:
    print("Smaller")
else:
    print("Bigger")



# Holy trinity

if a < b:
    print("Smaller")
elif a > b:
    print("Bigger")
else:
    print("Equal")

### Find out if 'number' is even or odd

number = random.randint(1, 100)
print('Number:', number)
# Write your code here

if number % 2 == 0:
    print('gerade')
else:
    print('ungerade')




"""

### Building a calculator (extra: check input operation)

firstInput = input("First Number: ")  # Returns a valid Integer
secondInput = input("Second Number: ")  # Returns a valid Integer
operandInput = input("Operation: ")  # Returns a String

try:
    first = int(firstInput)
    second = int(secondInput)
except (ValueError, AttributeError):
    print("Not a valid Number.")
else:
     # Write your code here
     pass
"""
