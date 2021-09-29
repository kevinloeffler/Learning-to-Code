import xtr

# Paramaterless functions

def showUsedBattery():
    capacity = xtr.cpc
    currentBattery = xtr.cur
    usedBattery = capacity - currentBattery
    print("You have used " + str(usedBattery) + "% Battery.")

# Parametric functions

word = "Remove"
cleanWord = word[0:-1]

def remove(string):
    string = string[0:-1]
    return string

a = remove("Anna")
b = remove("Kevin")

newWord = remove(word)

### Functional Calculator
# 4 basic operations: +, -, *, /
# 1 Advanced operations: n-power
# Calculations should be functions

def add (first, second):
    return first + second

def sub (first, second):
    return first - second



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
        result = add (first, second)
        print (result)
    elif operandInput == '-':
        result = sub (first, second)
        print (result)
