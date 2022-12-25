# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from math import *

def Difference(diff):
    size = int(input('Input size of array: '))
    array = []
    max = 0
    min = 1

    for _ in range(size):
        array.append(float(input('Input value of array: ')))
    print(f'Your array is: {array}')
    
    for i in range(len(array)):
        result = array[i] - floor(array[i])
        if result > max:
            max = result
        if min > result:
            min = result
        diff = max - min
    return(diff)

my_array = []
print(round(Difference(my_array), 2))