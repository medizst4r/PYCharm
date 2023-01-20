# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0
# или 10*x² = 0
# import random
#
# k_stepen = random.randint(1, 20)
# print(k_stepen)
#
#
# def polynomial(k):
#     list_polynomial = []
#     for i in range(k + 1):
#         koef = random.randint(0, 100)
#         if i == 0:
#             list_polynomial.append((f'{koef}'))
#         elif i == 1:
#             if koef != 0:
#                 list_polynomial.append((f'{koef}*x'))
#         else:
#             if koef != 0:
#                 list_polynomial.append((f'{koef}*x**{i}'))
#     list_polynomial.reverse()
#     return list_polynomial
#
#
# def list_to_function_str(list_polynomial):
#     sum = list_polynomial[0]
#     for i in list_polynomial[1::]:
#         if i[0] == '-':
#             i_rep = i.replace('-', '')
#             if i != list_polynomial[-1]:
#                 sum = sum + ' - ' + i_rep
#             elif len(list_polynomial) == 2:
#                 sum = sum + ' - ' + i_rep + ' = 0'
#             else:
#                 sum = sum + ' - ' + i_rep + ' = 0'
#         else:
#             if i != list_polynomial[-1]:
#                 sum = sum + ' + ' + i
#             elif len(list_polynomial) == 2:
#                 sum = sum + ' + ' + i + ' = 0'
#             else:
#                 sum = sum + ' + ' + i + ' = 0'
#     return sum
#
#
# list_polynomial_01 = polynomial(k_stepen)
# fun_01 = list_to_function_str(list_polynomial_01)
# print(fun_01)
# print()
#
# list_polynomial_02 = polynomial(k_stepen)
# fun_02 = list_to_function_str(list_polynomial_02)
# print(fun_02)
# print()
#
# list_polynomial_03 = polynomial(k_stepen)
# fun_03 = list_to_function_str(list_polynomial_03)
# print(fun_03)
#
# data = open('file01.txt', 'w')
# data.writelines(fun_01)
# data.close()
#
# data02 = open('file02.txt', 'w')
# data02.writelines(fun_02)
# data02.close()


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# g
