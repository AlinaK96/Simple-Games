'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''

from random import randint

print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока, делая свой выбор друг за другом\n'
)
print()
print(
        ' * Правила игры *\n'
    'У нас есть некоторое количество конфет\n'
    'За один ход можно забрать не более 28\n'
    'Тот, кому достанется последняя конфета - проиграл\n'
)

def choice(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def info(name, number, cout, total):
    print(f"Ходил {name}, он взял {number}, теперь у него {cout}. Осталось на столе {total} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
total = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 

if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

cout_player1 = 0 
count_player2 = 0

while total > 28:
    if flag:
        number = choice(player1)
        cout_player1 += number
        total -= number
        flag = False
        info(player1, number, cout_player1, total)
        print()
    else:
        number = choice(player2)
        count_player2 += number
        total -= number
        flag = True
        info(player2, number, count_player2, total)
        print()

if flag:
    print(f" {player1} - победил!")
else:
    print(f" {player2} - победил!")


# игра против бота:
from random import randint

def choice(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def info(name, number, count, total):
    print(f"Ходил {name}, он взял {number}, теперь у него {count}. Осталось на столе {total} конфет.")


def bot_calc(value):
    number = randint(1,29)
    while value-number <= 28 and value > 29:
        number = randint(1,29)
    return number

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
total = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 

if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count_player1 = 0 
count_player2 = 0

while total > 28:
    if flag:
        number = choice(player1)
        count_player1 += number
        total -= number
        flag = False
        info(player1, number, count_player1, total)
    else:
        number = bot_calc(total)
        count_player2 += number
        total -= number
        flag = True
        info(player2, number, count_player2, total)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")