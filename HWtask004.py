# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

quarternumber = int(input('Введите номер четверти плоскости: '))
if 4 < quarternumber or quarternumber < 1: print('Введено неверное число')
if quarternumber == 1: print('Диапазон возможных координат: x > 0, y > 0')
if quarternumber == 2: print('Диапазон возможных координат: x < 0, y > 0')
if quarternumber == 3: print('Диапазон возможных координат: x < 0, y < 0')
if quarternumber == 4: print('Диапазон возможных координат: x > 0, y < 0')