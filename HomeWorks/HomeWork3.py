#Задача 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def random_list_int(lenth, start, finish):
#     import random
#     random_list = []
#     for _ in range(lenth):
#         index = 0
#         random_list.append(int(random.uniform(start, finish)))
#     return random_list
#
# my_list = random_list_int(10,-10,10)
# print(my_list)
#
# negative_list = []
# sum = 0
# for i in my_list[::2]:
#     sum +=i
#     negative_list.append(i)
# print(f'Elements in odd positions - {negative_list} . Sum = {sum}')


#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# def random_list_int(lenth, start, finish):
#     import random
#     random_list = []
#     for _ in range(lenth):
#         index = 0
#         random_list.append(int(random.uniform(start, finish)))
#     return random_list
#
#
# list01 = random_list_int(10, -10, 10)
# list02 = random_list_int(9, -10, 10)
#
# def product_elements(my_list):
#     result = []
#     j = -1
#     i = 0
#     for _ in range(i, len(my_list)):
#         while i < (len(my_list)/2):
#             sum = my_list[i] * my_list[j]
#             result.append(sum)
#             j = j - 1
#             i = i + 1
#     return print(f'Product of numbers is {result}')
#
# print(list01)
# result01 = product_elements(list01)
#
# print(list02)
# result02 = product_elements(list02)


#Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def random_list_float(lenth, start, finish):
#     import random
#     random_list = []
#     for _ in range(lenth):
#         index = random.randint(0,3)
#         random_list.append(round(random.uniform(start, finish), index))
#     return random_list
#
# list01 = random_list_float(10, 0, 20)
# print(list01)
#
# list_str = []
# for i in list01:
#     list_str.append(str(i))
#
# list_point = []
# for i in list_str:
#     x = i.find('.')
#     list_point.append(x)
#
# list_result = []
# j = 0
# for i in list_str:
#     x=i[list_point[j]::]
#     a = '0'+x
#     list_result.append(float(a))
#     j += 1
# print(list_result)
#
# num_max = list_result[0]
# for i in list_result:
#     if i != 0:
#         num_min = i
#         break
#
# for i in list_result:
#     if i < num_min and i != 0:
#         num_min = i
#     elif i > num_max:
#         num_max = i
# result = round((num_max - num_min), 3)
# print(result)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
# import random
# num_start = random.randint(-100, 100)
# list_two_num = []
# if num_start < 0:
#     num = -1*num_start
# else:
#     num = num_start
#
# while num >= 1:
#     i = num % 2
#     num = num // 2
#     list_two_num.append(i)
# list_two_num.reverse()
#
# result = str(list_two_num[0])
# for i in list_two_num[1::]:
#     i = str(i)
#     result = result +i
#
# if num_start < 0:
#     result = '-' +result
# print(f'{num_start} В двоичной системе = {result}')