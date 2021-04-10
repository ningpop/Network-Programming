from socket import *
import random

BUF_SIZE = 1024
LENGTH = 20

# 수신한 message가 correct message인지 판별하는 함수
def is_msg_true(conn: socket, addr: tuple, recv_msg: bytes, correct_msg: bytes) -> bool:
    if not recv_msg: # 수신한 message가 비어있을 경우
        conn.close() # socket close
        return False
    elif recv_msg != correct_msg: # 수신한 message가 옳은 message가 아닌 경우
        print('client:', addr, msg.decode())
        conn.close() # socket close
        return False
    else: # 수신한 message가 옳은 message일 경우
        print('client:', addr, msg.decode())
        return True


sock = socket(AF_INET, SOCK_STREAM) # IPv4와 TCP로 소켓 연결
sock.bind(('', 11111)) # url과 port 번호 binding
sock.listen(10) # 최대 접속 소켓 수
print('Device 1 is running...')

while True:
    conn, addr = sock.accept()

    msg = conn.recv(BUF_SIZE) # msg 수신
    if msg != b'Request': # msg가 Request가 아닐 경우
        print('client:', addr, msg.decode())
        conn.close() # socket close
        continue
    if not is_msg_true(conn, addr, msg, b'Request'): # 수신한 msg 판별
        continue

    conn.send(b'Success') # client에게 연결 성공 msg 송신
    msg2 = conn.recv(BUF_SIZE) # client로부터 원하는 데이터 갯수 수신
    if not msg2:
        conn.close()
        continue
    how_much = int.from_bytes(msg2, 'big') # int type msg decode

    i = 1
    while True:
        if i > how_much: # 요청한 데이터 갯수만큼 반복
            break
        print(f'{i}/{how_much} data') # 데이터 갯수 체크

        temperature = random.randint(0, 40)
        humidity = random.randint(0, 100)
        illuminance = random.randint(70, 150)
        data = f'{temperature} {humidity} {illuminance}'
        conn.send(data.encode()) # device1의 데이터를 client에게 송신

        can_next = conn.recv(BUF_SIZE) # client로부터 다음번째 데이터로 넘어가도 되는지 여부 수신
        if not is_msg_true(conn, addr, can_next, b'next'): # 수신한 msg 확인
            break

        i += 1

    msg3 = conn.recv(BUF_SIZE) # quit msg 수신
    if msg3.decode() == 'quit':
        conn.close()