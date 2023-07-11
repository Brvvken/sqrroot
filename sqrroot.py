import math

while True:
    num = float(input('Enter a number: '))

    print('The square root of %0.3f is %0.3f' % (num, math.sqrt(num)))

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
         break