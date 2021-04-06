from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    formula = input('>> ') # 계산 식 입력
    if formula == 'q':
        break

    s.send(formula.encode()) # 계산식 encoding 후 server에 전송

    print('result:', s.recv(1024).decode()) # 계산된 결과값을 수신하여 decoding 후 출력

s.close()