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
