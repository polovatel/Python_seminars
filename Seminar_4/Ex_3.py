# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

def Unique_numbers(array):
    size = int(input('Input size of array: '))
    array = []
    unique_array = []

    for i in range(size):
        array.append(int(input('Input values of array: ')))

    for j in range(size):
        if array[j] in unique_array:
            continue
        else:
            unique_array.append(array[j])
    return unique_array


My_array = []
print(Unique_numbers(My_array))


