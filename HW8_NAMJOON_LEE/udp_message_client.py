from socket import *

BUFF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM) # IPv4, UDP
sock.connect(('localhost', port)) # UDP이지만 설정 시 TCP처럼 동작 가능

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):') # 명령어와 메시지 입력
    if msg == 'quit': # quit 입력시 종료
        sock.close()
        break
    sock.send(msg.encode()) # 메시지 송신
    print(sock.recv(BUFF_SIZE).decode()) # 수신 메시지 출력