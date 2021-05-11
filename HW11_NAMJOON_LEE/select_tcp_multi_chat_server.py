import socket, select
import time
import threading

socks = []

def chat(sock: socket):
    data = sock.recv(1024) # 메시지 수신

    if 'quit' in data.decode(): # quit 입력 시
        print(sock, 'exited')
        sock.close()
        socks.remove(sock) # 해당 client 삭제
        return

    print(time.asctime() + str(sock.getsockname()) + ':' + data.decode()) # client 메시지 log 출력

    for client in socks: # clients 리스트 순회
        if client != sock and client != s: # 송신 client와 처음 연결된 socket을 제외한 나머지 client에게
            client.send(data) # 메시지 송신

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
s.bind(('', 2500))
s.listen(5)
socks.append(s)
print('2500에서 접속 대기 중')

print('Server Started')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], []) # select를 사용한 I/O Multiplexing

    for sock in r_sock: # 이벤트 처리된 socket 순회
        if sock == s: # 처음 소켓 연결 시
            conn, addr = s.accept()
            socks.append(conn) # 소켓 리스트에 추가
            print('Client ({}) connected'.format(addr))
        else:
            chat(sock) # 해당 소켓으로 멀티채팅 시작