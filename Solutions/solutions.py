### 2. Numbers:
result = 9.0 # (Float)

### 3. Conditions

# 3.1 Even or Odd?
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3.2 Calculator

firstInput = input("First Number: ")  # Returns a valid Integer
operandInput = input("Operation: ")  # Returns a String
secondInput = input("Second Number: ")  # Returns a valid Integer

try:
    first = int(firstInput)
    second = int(secondInput)
except (ValueError, AttributeError):
    print("Not a valid Number.")
else:
    if operandInput == '+':
         print(first + second)
    elif operandInput == '-':
         print(first - second)
    elif operandInput == '/':
         print(first / second)
    elif operandInput == '*':
         print(first * second)
    else:
         print("Not a valid operation, choose + | - | * | /")



while True:
    number = int(input(str(counter) + ". Number: "))
    if number == 0:
        break
    else:
        result += number

print(result)


    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    result = 1
    for i in range(num2):
        result = multiply(result, num1)
    return result

def root(num1, num2):
    result = 1
    counter = 0
    while result < num1:
        result += power(result, 2)
        counter += 1
    return counter

print(root(1024, 5))
