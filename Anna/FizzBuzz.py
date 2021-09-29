# / 3 = Fizz
# / 5 = Buss
# / 15 = FizzBuzz

for x in range (1, 101):

    if x % 15 == 0:
        print ('FizzBuzz')
    elif x % 3 == 0:
        print ('Fizz')
    elif x % 5 == 0:
        print ('Buss')
    else:
        print (x)
