from random import randint

player = 50

while True:
    if player <= 0 or player >= 100:
        print('GAME OVER')
        break

    coin = randint(1, 2)
    guess = int(input('앞면? or 뒷면?(앞면은 1, 뒷면은 2 입력) : '))
    
    if guess == coin:
        player += 9
        print(f'맞았습니다! $9를 따서 ${player}가 되었습니다.')
    else:
        player -= 10
        print(f'틀렸습니다! $10를 잃어 ${player}가 되었습니다.')

    print('========================================')