# Запросити у користувача число N, вивести всі числа від 0 до N, які діляться на 3.
# Запросити у користувача число N, вивести суму чисел від 0 до N. Які поділяються на 3 без залишку.

# variables
N = input('Please enter your number: ')
current_number = 1
sum = 0

# in case user has entered not a number
try:
    N = int(N)
except ValueError:
    print('Please use only whole numbers')
    exit()

# cycle
while N > current_number:
    if current_number % 3 == 0:
        # showing the number if it divides by 3 without a remainder
        print(current_number, ' is between 0 and your number and divides by 3 without a remainder')
        # adding the number into sum if it divides by 3 without a remainder
        sum += current_number
    current_number += 1
print('\nThe sum of numbers from 0 to your number that divide by 3 without a remainder is equal to', sum)