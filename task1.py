# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


total_sweets = int(input('Введите количество всех конфет: '))

player1 = 1
player2 = 2


def sweets(player):
    x = int(input('Введите количество конфет, которые возьмёте за этот ход: '))
    if x < 1 or x > 28:
        x = int(input('ошибка! Введите верно: '))
    return x


player1 = True


while total_sweets > 28:
    if player1 == True:
        print('Ходит player1')
        i = sweets(player1)
        total_sweets -= i
        print(f'осталось {total_sweets} конфет')
        player1 = False
    else:
        print('Ходит player2')
        i = sweets(player2)
        total_sweets -= i
        print(f'осталось {total_sweets} конфет')
        player1 = True

if player1 == False:
    print('Выиграл player1')
else:
    print('Выиграл player2')
