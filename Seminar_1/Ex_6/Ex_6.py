#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
from math import *
a = float(input())

if a - floor(a) != 0:
    print(floor(a * 10)%10)
else:
    print('Дробной части нет!')

# from math import *
# a = float(input())

# if a - trunc(a) != 0:
#     print(trunc(a * 10)%10)
# else:
#     print('Дробной части нет!!!!!!!!')
