import random

# What if...

yes = True
no = False

if yes:
    pass
    #print("Yay")

if no:
    print("Nope")


# Comparisons: > < ==

a = 3
b = 3

if a > b:
    pass
    #print("Bigger")


# Nespresso, what else

if a < b:
    print("Smaller")
else:
    print("Bigger")



# Holy trinity

if a < b:
    print("Smaller")
elif a > b:
    #print("Bigger")
    pass
else:
    print("Equal")

### Find out if 'number' is even or odd

number = random.randint(1, 100)
print('Number:', number)

if number % 2 == 0:
    print ("even")
else:
    print ("odd")
