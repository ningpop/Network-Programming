import socket
import time
import threading

clients = [] # clients 리스트

def chat(sock: socket):
    while True:
        data = sock.recv(1024) # 메시지 수신

        if 'quit' in data.decode(): # quit 입력 시
            print(sock, 'exited')
            clients.remove(sock) # 해당 client 삭제
            continue

        print(time.asctime() + str(sock.getsockname()) + ':' + data.decode()) # client 메시지 log 출력

        for client in clients: # clients 리스트 순회
            if client != sock: # 송신 client를 제외한 나머지 client에게
                client.send(data) # 메시지 송신

    sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
s.bind(('', 2500))
s.listen(5)

print('Server Started')

while True:
    conn, addr = s.accept()
    if addr not in clients: # 신규 client일 때
        clients.append(conn) # client 목록에 추가
        print('connected by', addr)
        th = threading.Thread(target=chat, args=(conn, )) # 멀티스레드를 활용하여 송수신
        th.start()