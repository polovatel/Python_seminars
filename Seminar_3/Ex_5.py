# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] ````

def Fibonacci(size):
    size = int(input('Input size of array: '))
    array = []
    a, b = 1, 1

    for i in range(size):
        array.append(a)
        a, b = b, a + b
    a, b = 0, 1

    for j in range(size + 1):
        array.insert(0,a)
        a,b = b, a - b

    return(array)

My_array = []
print(Fibonacci(My_array))