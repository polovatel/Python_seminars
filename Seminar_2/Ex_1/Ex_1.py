# 1) Напишите программу, которая принимает на вход число N и выдаёт последовательность размера N из чередующихся по знаку степеней тройки.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

from math import *
n = int(input())

for i in range(n):
    if i % 2 == 1:
        print(-3**i)
    else:
        print(3**i)