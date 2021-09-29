# Can you repeat that for me?

for i in range(10):
    print(i)

list = [1, 2, 3, 4, 5]

for element in list:
    print(element)

x = 0
amount = 10

for i in range(amount):
    x += i

print(x)

# To infinity and beyond

while False:
    print("Hello")

counter = 0

while counter < 10:
    print("Still below 10")
    counter += 1

### Build a counter

counter = 1
result = 0

print("This App lets you add as many numbers as you like.")
print("Input 0 to calculate the result.")

while True:
    number = int(input(str(counter) + ". Number: "))
    if number == 0:
        break
    else:
        result += number

print(result)
