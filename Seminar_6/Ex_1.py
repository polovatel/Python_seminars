# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

array = list(map(int, input('Input values of array through space button: ').split()))

def filter_my_list(number):
    if 100 > number >= 10:
        return True
    else:
        return False

result = filter(filter_my_list, array)
print(f'Your filtered array is: {list(result)}')

