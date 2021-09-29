# Numbers:
result = 9.0  # (Float)


# Even or Odd?
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Counter 1
counter = 1

while True:
    number = int(input(str(counter) + ". Number: "))
    if number == 0:
        break
    else:
        result += number
        counter += 1

print("Your result is:", result)


# Counter 2
userInput = None
counter = 1

while userInput != 0:
    userInput = int(input(str(counter) + ". Number: "))
    result += userInput
    counter += 1

print("Your result is:", result)


# Calculator
def power(num1, num2):
    result = 1
    for i in range(num2):
        result = result * num1
    return result

def root(num1, num2):
    result = 1
    counter = 0
    while result < num1:
        result += power(result, 2)
        counter += 1
    return counter

print(root(1024, 5))
