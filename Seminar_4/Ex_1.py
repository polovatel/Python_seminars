# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ round())

from math import pi

p = str(pi)
count = int(input('Input size of digits after ",": '))

print(p[:count+2])