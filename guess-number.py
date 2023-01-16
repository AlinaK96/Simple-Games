print("Загадайте число от 0 до 100, а я попытаюсь его отгадать")		
		
import random		
number = random.randint(0, 100)		
print(number)		
user_number = None		
		
levels = {1: 10, 2: 5, 3: 3}		
level = int(input("Выберете один из трёх уровней сложности: "))		
max_count = levels[level]		
		
user_count = int(input("Введите количество пользователей: "))		
users = []		
for i in range(user_count):		
    i+=1		
    user_name = input(f"Введите имя {i} пользователя: ")		
    users.append(user_name)		
print(f"Игроки: {users}")		
		
winner = False		
winner_name = None		
while not winner:		
    print(f"Осталось попыток: {max_count}")		
    max_count-=1		
    if max_count < 0:		
        print(f"К сожалению попыток больше нет. Правильный вариан: {number}")		
        break		
    for user in users:
        print(f"Победа! Загаданное число: {number}. Победитель:  {winner_name}!")		
