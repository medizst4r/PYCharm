# # Задача 1
#  Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
#import random
#
#
# def meeting():
#     user_name = input("Player, what is your name? ")
#     print(f'{user_name}, welcome!\n Good luck! ')
#     return user_name
#
#
# player = meeting()
# user_name = [player, 'Bot']
#
# all_candy = random.randint(10, 200)
# print(f'{all_candy} - all candies on the table.')
#
# level_input = int(input(f'Input level: \n 1 - easy \n 2 - hard \n'))
# while level_input not in range(1, 3):
#     level_input = int(input(f'Input level: \n 1 - easy \n 2 - hard \n'))
# level = [1, 2]
#
# taken_candy = 0
# first_move = random.choice(user_name)
# print(f'Player {first_move}  goes first!')
#
#
# def move_player(player, taken, all):
#     count = int(input(f'{player}, how many candies you take? : '))
#     while count not in range(1, 29):
#         count = int(input(f'{player}, input a number from 1 to 28. How many candies you take? : '))
#     taken = taken + count
#     print(f'{all - taken} - leftover candies')
#     return taken
#
#
# def move_bot(taken, all):
#     count = random.randint(1, 28)
#     print(f'{count} - taken Bot. ')
#     taken = taken + count
#     print(f'{all - taken} - leftover candies')
#     return taken
#
#
# def move_bot_hard(taken, all):
#     x = (all - taken) // 28
#     a = (all - taken) - x * 28 - 1
#     if (all - taken) / 28 <= 1:
#         a = all - taken
#     if a in range(-1, 1):
#         a = 1
#     count = a
#     print(f'{count} - taken Bot. ')
#     taken = taken + count
#     print(f'{all - taken} - leftover candies')
#     return taken
#
#
# for i in user_name:
#     if i != first_move:
#         second_move = i
#
# user_name[0] = first_move
# user_name[1] = second_move
#
# if level_input == level[0]:
#     while True:
#         if user_name[0] in 'Bot':
#             taken_candy = move_bot(taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'Bot - winner!')
#                 break
#         elif user_name[0] not in 'Bot':
#             taken_candy = move_player(user_name[0], taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'{i} - winner!')
#                 break
#         if user_name[1] in 'Bot':
#             taken_candy = move_bot(taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'Bot - winner!')
#                 break
#         elif user_name[1] not in 'Bot':
#             taken_candy = move_player(user_name[1], taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'{i} - winner!')
#                 break
#
# elif level_input == level[1]:
#     while True:
#         if user_name[0] in 'Bot':
#             taken_candy = move_bot_hard(taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'Bot - winner!')
#                 break
#         elif user_name[0] not in 'Bot':
#             taken_candy = move_player(user_name[0], taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'{i} - winner!')
#                 break
#         if user_name[1] in 'Bot':
#             taken_candy = move_bot_hard(taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'Bot - winner!')
#                 break
#         elif user_name[1] not in 'Bot':
#             taken_candy = move_player(user_name[1], taken_candy, all_candy)
#             if taken_candy > all_candy - 1:
#                 print(f'{i} - winner!')
#                 break


# Задача 2 Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
# import random
# win_field = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
#              [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
#
# def print_field(field):
#     print(*(field[0][0], field[1][0]), field[2][0])
#     print(*(field[0][1], field[1][1]), field[2][1])
#     print(*(field[5][0], field[5][1]), field[5][2])
#
# print_field(win_field)
#
# user_name = ['Player', 'Bot']
# plus = '+'
# zero = '0'
# print(f'{user_name[0]} - {plus}.\n{user_name[1]} - {zero}')
#
# def winner_is(field, simbol):
#     for i in field:
#         if i == [simbol, simbol, simbol]:
#             return True
#
# list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# field_bot = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
#              [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
#
# def move_player(field, user, simbol, num, bot):
#     move_us = int(input(f'{user}, input the number: '))
#     while move_us not in num:
#         move_us = int(input(f'{user}, input the number: '))
#     for i in range(len(field)):
#         for j in range(3):
#             if field[i][j] == move_us:
#                 field[i][j] = simbol
#     num = list(filter((lambda i: i != move_us), num))
#     bot = list(filter((lambda i: move_us not in i), bot))
#     return field, num, bot
#
# def move_bot(field, user, simbol, num, bot):
#     if len(bot) != 0:
#         for e in bot:
#             for j in e:
#                 move_us = random.choice(e)
#     else:
#         move_us = random.choice(num)
#     print((f'{user}, input the number {move_us}'))
#     for i in range(len(field)):
#         for j in range(3):
#             if field[i][j] == move_us:
#                 field[i][j] = simbol
#     num = list(filter((lambda i: i != move_us), num))
#     for e in bot:
#         for j in e:
#             if j == move_us:
#                 e.remove(j)
#     return field, num, bot
#
# while True:
#     win_field, list_num, field_bot = move_player(
#         win_field, user_name[0], plus, list_num, field_bot)
#     print_field(win_field)
#     x = winner_is(win_field, plus)
#     if x == True:
#         print(f'{user_name[0]} - winner!')
#         break
#
#     if len(list_num) == 0:
#         print('End!')
#         break
#
#     win_field, list_num, field_bot = move_bot(
#         win_field, user_name[1], zero, list_num, field_bot)
#     print_field(win_field)
#     x = winner_is(win_field, zero)
#     if x == True:
#         print(f'{user_name[1]} - winner!')
#         break

# Задача 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
# import string
# data_open = open('HomeWork05/text1.txt', 'r')
# data = data_open.read()
# data_open.close()
# print(data)
#
# new_data = set(data)
# new_data = sorted(list(new_data))
# num = []
# for i in new_data:
#     if i in data:
#         x = data.count(i)
#         num.append(x)
#
# result = str(str(num[0]) + str(new_data[0]))
# for i in range(1, len(num)):
#     result = result + str(num[i]) + str(new_data[i])
# print(result)
# result = result
#
# alph = []
# for i in result:
#     if i in string.ascii_lowercase:
#         alph.append(i)
#
# for i in alph:
#     result = result.replace(i, ' ')
# nums = result.split()
# nums = list(map(int, nums))
# print(nums)
# my_revers = alph[0]*nums[0]
# for i in range(1, len(alph)):
#     my_revers = my_revers + alph[i]*nums[i]
# print(my_revers)
#
# data_write = open('HomeWork05/text_write.txt', 'w')
# data_write.writelines(my_revers)
# data_write.close()