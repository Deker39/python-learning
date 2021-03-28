import  random

player_result = ''
com_result = ''
win = 0
com = random.randint(1,3)
player = int(input("1 - камеь, 2 - ножницы, 3 - бумага \nЧто выбираешь ты: "))

#choice player
if player == 1:
    player_result = 'камень'
if player == 2:
    player_result = 'ножницы'
if player == 3:
    player_result = 'бумага'
#choice computer
if com == 1:
    com_result = 'камень'
if com == 2:
    com_result = 'ножницы'
if com == 3:
    com_result = 'бумага'

print(player_result + " vs " + com_result)

if player == com:
        win = 0
if player == 1 and com == 2:
        win = 1
if player == 1 and com == 3:
        win = 2
if player == 2 and com == 1:
        win = 2
if player == 2 and com == 3:
        win = 1
if player == 3 and com == 1:
        win = 1
if player == 3 and com == 2:
        win = 2
if win == 0:
        print("Ничья!")
if win == 1:
        print("Победил игрок!")
if win == 2:
        print("Победил компьютер!")