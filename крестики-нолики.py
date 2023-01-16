'''Создайте программу для игры в "Крестики-нолики"'''

def game_field(field):
    print('-' * 13)
    for i in range (3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-' * 13)

def take_input(player_name):
    valid = False
    while not valid:
        move = input('В какой клетке будет ' + player_name + ' ')
        try:
            move = int(move)
        except ValueError:
            print('Введите число от 0 до 9')
            continue
        if 1 <= move <= 9:
            if str(field[move - 1]) not in 'X0':
                field[move - 1] = player_name
                valid = True
            else:
                print('Это место уже занято ')
        else:
            print('Введите число от 1 до 9')

def winner(field):
    position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in position:
        if field[each[0]] == field[each[1]]== field[each[2]]:
            return field[each[0]]
    return False

def main(field):
    counter = 0
    win = False
    while not win:
        game_field(field)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('0')
        counter += 1
        if counter > 4:
            tmp = winner(field)
            if tmp:
                game_field(field)
                print(tmp, ' победил!')
                win = True
                break
            if counter == 9:
                game_field(field)
                print('Ничья!')
                break
            game_field(field)
print('Игра Крестики-нолики для двух игроков ')
field = list(range(1,10))
main(field)
input('Нажмите Enter чтобы начать сначала! ')

