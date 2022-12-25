#даны 2 числа, проверить что a / b, если да - "Да", нет - "Нет"

a, b = int(input()), int(input())

if b != 0:
    if a % b == 0:
        print('Да')
    else:
        print('НЕТ')

else:
    print('На ноль делить нельзя')