# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции. - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def count_sum(total):
    size = int(input('Input size of array: '))
    array = []
    total = 0
    
    for i in range(size):
        array.append(int(input('Input values of array: ')))
    print('Your array is:', array)

    for i in range(1, len(array), 2):
        total += array[i]
    return total

my_array= []
print(count_sum(my_array))


    
    
