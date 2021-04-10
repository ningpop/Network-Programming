from socket import *
from datetime import datetime

BUF_SIZE = 1024
LENGTH = 20

# device1의 data 출력
def print_for_device_1(data: str, now: datetime):
    data_list = data.split()
    week = now.strftime("%a %b %d %H:%M:%S %Y") # 현재시간의 날짜 형식 지정
    writing_data = f'{week}: Device1: Temp={data_list[0]} Humid={data_list[1]} Illum={data_list[2]}'
    print(writing_data)

    f = open('data.txt', 'a')
    f.write(writing_data + '\n') # 파일 출력
    f.close()

# device2의 data 출력
def print_for_device_2(data: str, now: datetime):
    data_list = data.split()
    week = now.strftime("%a %b %d %H:%M:%S %Y") # 현재시간의 날짜 형식 지정
    writing_data = f'{week}: Device2: Heartbeat={data_list[0]} Steps={data_list[1]} Cal={data_list[2]}'
    print(writing_data)

    f = open('data.txt', 'a')
    f.write(writing_data + '\n') # 파일 출력
    f.close()

# device로부터 data 가져오는 함수
def get_data_from_device(sock: socket, port: int):
    sock.connect(('', port)) # url과 port로 socket 연결

    sock.send(b'Request') # Request 메시지 전송
    if sock.recv(BUF_SIZE) != b'Success': # device로부터 받은 메시지의 연결 성공 여부 확인
        print('Fail device connection.')
        sock.close()
        return
    print('Success device connection.')

    data_count = int(input('How much data do you need? ')) # 사용자로부터 원하는 데이터 갯수 입력
    sock.send(data_count.to_bytes(4, 'big')) # 해당 device로 데이터 갯수 송신

    i = 1
    while True:
        if i > data_count: # 데이터 갯수만큼 반복
            break
        data = sock.recv(BUF_SIZE).decode() # device로부터 측정값 데이터 수신
        now = datetime.now() # 수신한 날짜&시각 측정
        if port == 11111:
            print_for_device_1(data, now) # device1과 device2 구분하여 값 출력
        elif port == 22222:
            print_for_device_2(data, now) # device1과 device2 구분하여 값 출력
        print(f'==========> {i}/{data_count} data') # 몇번째 데이터인지 카운트
        sock.send(b'next') # 다음 데이터로 넘어가도 된다는 msg 송신
        i += 1

# device의 socket을 close하는 함수
def close_socket_of_device(sock: socket):
    sock.send(b'quit')
    sock.close()

s1 = socket(AF_INET, SOCK_STREAM) # IPv4와 TCP로
s2 = socket(AF_INET, SOCK_STREAM) # IPv4와 TCP로

while True:
    order = input('choose device number(if you close connection, insert "quit"): ')
    if order == '1': # device1을 선택한 경우
        get_data_from_device(s1, 11111)
    elif order == '2': # device2을 선택한 경우
        get_data_from_device(s2, 22222)
    elif order == 'quit': # device들을 모두 종료
        close_socket_of_device(s1)
        close_socket_of_device(s2)
        break
    else:
        print('Wrong input data.')