import xtr

# Paramaterless functions

def showUsedBattery():
    capacity = xtr.cpc
    currentBattery = xtr.cur
    usedBattery = capacity - currentBattery
    print("You have used " + str(usedBattery) + "% Battery.")

showUsedBattery()

# Parametric functions

word = "Remove!"
cleanWord = word[0:-1]

def remove(string):
    string = string[0:-1]
    return string

newWord = remove(word)
print(newWord)

### Functional Calculator
# 4 basic operations: +, -, *, /
# 1 Advanced operations: n-power
# Calculations should be functions

def multiply(num1, num2):
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
