# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и вывести многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 
# k = 6
# ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
# a, b, c, d, e, h - рандом

import random
import math

digit = int(input())
a = [random.randint(0,100) for i in range(digit + 1)]
text= ''

for i in range(digit, 0, - 1):
    if i == 1:
        text += str(a[i]) + 'x + ' + str(a[i + 1])
    else:
        text += str(a[digit - i]) + 'x^' + str(i) + ' + '
    
print(text)
   
    





