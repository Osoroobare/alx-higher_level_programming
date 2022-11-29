#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(1, 10):
        if number2 > number1:
            print("{}{}".format(number1, number2), end='')
            if int(str(number1) + str(number2)) != 89:
                print(end=', ')
print()
            
