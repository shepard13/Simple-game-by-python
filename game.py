import random

from position import user_position, enemy_position, defences_position







from square import square

user_name = input('Enter your name: ')
print(f'{user_name.upper()} Welcome to the PyHunter!')
character = input('Choose the character["@" - vimpire, "#" - humman]: ')
if character == "@":
    print(f'You picked the Vampire: {character}')
    print('You are VAMPIRE your enemy is HUMAN "#"')

    enemy_position['x'] = random.randint(1, 9)
    enemy_position['y'] = random.randint(1, 9)
    square[enemy_position['y']][enemy_position['x']] = '#'
    defences_position['x'] = random.randint(1, 9)
    defences_position['y'] = random.randint(1, 9)
    square[defences_position['y']][defences_position['x']] = 'X'
else:
    print(f'You picked the Humman: {character}')
    print('You are HUMMAN your enemy is VAMPIRE "@"')
    enemy_position['x'] = random.randint(1, 9)
    enemy_position['y'] = random.randint(1, 9)
    square[enemy_position['y']][enemy_position['x']] = '@'
    defences_position['x'] = random.randint(1, 9)
    defences_position['y'] = random.randint(1, 9)
    square[defences_position['y']][defences_position['x']] = 'X'
# Strat coordinates of coin and user positions
square[user_position['y']][user_position['x']] = character

for sublist in square:
    print(*sublist)
square[user_position['y']][user_position['x']] = '.'

score = 0

while True:
    moves = input(f'{user_name.upper()} Enter the direction[UP, DOWN, LEFT, RIGHT]: ')

    if score == 5:
        print('VICTORY!!!')
        print(score)
        break

    if user_position == defences_position:
        print('GAME OVER!')
        break
    if user_position == enemy_position:
        enemy_position['x'] = random.randint(1, 9)
        enemy_position['y'] = random.randint(1, 9)
        defences_position['x'] = random.randint(1, 9)
        defences_position['y'] = random.randint(1, 9)
        if character == '@':
            square[enemy_position['y']][enemy_position['x']] = '#'
            square[defences_position['y']][defences_position['x']] = 'X'
            score += 1
        elif character == '#':
            square[enemy_position['y']][enemy_position['x']] = '@'
            square[defences_position['y']][defences_position['x']] = 'X'
            score += 1

    # MOVE LEFT FOR ALL CHARACTERS
    if moves.upper() == 'LEFT':
        if character == '@':
            print('You have ultimate skill, Enter the step')
            pos = int(input('Enter the Step but not more then 4:  '))
            user_position['x'] -= pos
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'
            print(square)
        else:
            user_position['x'] -= 1
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'

    # MOVE RIGHT FOR ALL CHARACTERS
    if moves.upper() == 'RIGHT':
        if character == '@':
            print('You have ultimate skill, Enter the step')
            pos = int(input('Enter the Step but not more then 4:  '))
            user_position['x'] += pos
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'
        else:
            user_position['x'] += 1
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'

    # MOVE UP FOR ALL CHARACTERS
    if moves.upper() == 'UP':
        if character == '@':
            print('You have ultimate skill, Enter the step')
            pos = int(input('Enter the Step but not more then 4: '))
            user_position['y'] -= pos
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'
        else:
            user_position['y'] -= 1
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'

    # MOVE DOWN FOR ALL CHARACTERS
    if moves.upper() == 'DOWN':
        if character == '@':
            print('You have ultimate skill, Enter the step')
            pos = int(input('Enter the Step but not more then 4:  '))
            user_position['y'] += pos
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'
        else:
            user_position['y'] += 1
            square[user_position['y']][user_position['x']] = character
            print(f'Score: {score}')
            print(f'{user_name.upper()} your posiition is {user_position}')
            for sublist in square:
                print(*sublist)
            square[user_position['y']][user_position['x']] = '.'

    if moves.upper() == ('Q' or 'E' or 'EXIT' or 'QUIT'):
        break
