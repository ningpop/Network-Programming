import socket
import threading

# 멀티스레드용 메시지 수신 함수
def handler(sock: socket):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode()) # ID 송신

th = threading.Thread(target=handler, args=(sock, )) # 멀티스레드를 활용하여 송수신
th.daemon = True # 메인 스레드가 종료되면 하위 스레드도 종료
th.start()

while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode()) # 메시지 입력받고 송신