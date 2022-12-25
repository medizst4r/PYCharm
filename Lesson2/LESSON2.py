# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') # Создание текстовой переменной и связываем ее с текстовый файлом, в скобках путь к файлу и мод
# data.writelines(colors) # разделителей не будет
# data.close()  #  закрытие подключения к файлу

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
#
# exit()


# Функции и модули

# import hello
# print(hello.f(1)) #папки разные, не сработало

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))  #asdw
# print(concatenatio('a', '1'))  #a1


# Рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# Кортежи - это неизменяемый список

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res
# a = (3,4)
# print(a)


# Словари - неупорядоченные коллекции произвольных обьектов с доступом по ключу
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
#
# for k in dictionary.keys():
#     print(k)
# # типы ключей могут отличаться

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # c = {1, 2, 3, 5, 8}
# u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)   # i = {8, 2, 5}
# dl = a.difference(b)    # dl = {1, 3}
# dr = b.difference(a)    # dr = {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}
# s= frozenset(a)

# Списки
# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)
#
# print()
# for e in list2:
#     print(e)
#

