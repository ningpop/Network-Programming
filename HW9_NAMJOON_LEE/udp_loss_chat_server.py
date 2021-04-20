from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM) # IPv4, UDP
sock.bind(('', port)) # binding

while True:
    sock.settimeout(None) # timeout 초기화
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE) # 메시지 받음
        if random.random() <= 0.5: # 50%의 확률 발생
            continue
        else:
            sock.sendto(b'ack', addr) # 정상 수신이므로 ack 전송
            print('<-', data.decode()) # 받은 메시지 출력
            break
    
    msg = input('-> ') # server의 메시지 입력
    reTx = 0 # 재전송 횟수 초기화
    while reTx <= 3: # 재전송 횟수 추가 3회까지 제한
        resp = str(reTx) + ' ' + msg # 재전송 횟수와 메시지를 결합
        sock.sendto(resp.encode(), addr) # 메시지 전송
        sock.settimeout(2) # timeout 2초로 설정

        try:
            data, addr = sock.recvfrom(BUFF_SIZE) # ack을 받음. timeout시 except구문으로 이동
        except timeout:
            reTx += 1 # 재전송 횟수 1 증가
            continue
        else:
            break # timeout이 일어나지 않았으므로 통과