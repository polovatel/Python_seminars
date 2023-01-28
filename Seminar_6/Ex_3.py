# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum_digit(number):
    return sum(map(int, number.replace('.', '').replace('-', '')))

num = input('Input real number: ')
print(f'Som of digits in real number is: {sum_digit(num)}')
