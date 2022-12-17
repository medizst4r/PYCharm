# Задача 1.Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Input a number from 1 to 7 :')
n = int(input())

weekday = range(1,6)
weekend = range(6,8)

while not n in weekday and not n in weekend :
    print('Input a number from 1 to 7 :')
    n = int(input())

if n in weekday :
    print(f'{n} - weekday :)')
elif n in weekend:
    print(f'{n} - weekend !')

# Задача 3 Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print ('Please, input X :')
x = int(input())
print ('Please, input Y :')
y = int(input())

while x == 0 or y == 0:
    print('The wrong number!!!')
    print ('Please, input X :')
    x = int(input())
    print ('Please, input Y :')
    y = int(input())

if x > 0 and y > 0 :
    print (f'{x} and {y} - 1 quarter')
elif x < 0 and y > 0 :
    print (f'{x} and {y} - 2 quarter')
elif x < 0 and y < 0 :
    print (f'{x} and {y} - 3 quarter')
elif x > 0 and y < 0 :
    print (f'{x} and {y} - 4 quarter')

# Задача 4  Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
quart_list = [1, 2, 3, 4]
plus = 'from 0 to plus infinity'
minus = 'from 0 to minus infinity'

user = int(input(f'Input a number of the quarter : 1 or 2 or 3 or 4 : '))

while user not in quart_list:
    print = ('The wrong number !!!')
    user = int(input(f'Input a number of the quarter  1 or 2 or 3 or 4 : '))

if user == quart_list[0]:
    print (f' Range {user} of the quarter: \n X {plus}  \n Y {plus}')
elif user == quart_list[1]:
    print (f' Range {user} of the quarter: \n X {minus}  \n Y {plus}')
elif user == quart_list[2]:
    print (f' Range {user} of the quarter: \n X {minus}  \n Y {minus}')
elif user == quart_list[3]:
    print (f' Range {user} of the quarter: \n X {plus}  \n Y {minus}')

Задача 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
point_a = []
for i in range(2):
    point_a.append(int(input('Input coordinate point A pressing ENTER:')))

point_b = []
for i in range(2):
    point_b.append(int(input('Input coordinate point B pressing ENTER:')))

print('Coordinate A:', point_a, 'Coordinate B:', point_b)

if point_b[0] > point_a[0]:
    ac = point_b[0] - point_a[0]
else:
    ac = point_a[0] - point_b[0]

if point_b[1] > point_a[1]:
    bc = point_b[1] - point_a[1]
else:
    bc = point_a[1] - point_b[1]

ab = round(math.sqrt(ac**2 + bc**2),2)
print('Lenght AB = ', ab)