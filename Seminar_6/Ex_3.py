# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

real_number = int(input('Input real number: '))

sum_of_digits = sum(map(int, str(real_number)))
print(sum_of_digits)