# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# str_list = []
# str_list = input('Input a real number: ')
#
# sum = 0
# for number in str_list:
#     if number == '.' or number == '-':
#         del number
#     else:
#         sum += int(number)
# print('The sum of the digits of your number:' , sum)


# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# num = (input('Input a  positive integer number: '))
# while num.isdigit() != True:
#     num = (input('Input a  positive integer number: '))
#
# num = int(num)
# num_list = []
# sum = 0
#
# for i in range(1, num + 1, 1):
#     num_list.append(round(float(1 / i + 1) ** i, 2))
# print(f'The list of {num} - {num_list}')
#
# for i in num_list:
#     sum += i
# print('The sum of the elements of the list: ', sum)


# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

# from random import randint
# no_mix = range(20)
#
# print(list(no_mix))
#
# mix_list = []
# for i in no_mix:
#     i = randint(0,len(no_mix)-1)
#     while len(no_mix) != len(mix_list):
#         i = randint(0,len(no_mix)-1)
#         if i not in mix_list:
#             mix_list.append(i)
#         else:
#             del i
# print(mix_list)