import selectors
import socket
from datetime import datetime

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

def read1(conn, mask): # 기존 클라이언트로부터 수신한 데이터를 처리하는 함수
    i = 1
    while True:
        if i > 5: # 데이터 갯수만큼 반복
            break
        data = conn.recv(1024).decode() # device로부터 측정값 데이터 수신
        now = datetime.now() # 수신한 날짜&시각 측정
        print_for_device_1(data, now) # device1과 device2 구분하여 값 출력
        print(f'==========> {i}/{5} data') # 몇번째 데이터인지 카운트
        conn.send(b'next') # 다음 데이터로 넘어가도 된다는 msg 송신
        i += 1

def read2(conn, mask): # 기존 클라이언트로부터 수신한 데이터를 처리하는 함수
    i = 1
    while True:
        if i > 5: # 데이터 갯수만큼 반복
            break
        data = conn.recv(1024).decode() # device로부터 측정값 데이터 수신
        now = datetime.now() # 수신한 날짜&시각 측정
        print_for_device_2(data, now) # device1과 device2 구분하여 값 출력
        print(f'==========> {i}/{5} data') # 몇번째 데이터인지 카운트
        conn.send(b'next') # 다음 데이터로 넘어가도 된다는 msg 송신
        i += 1


sock1 = socket.socket()
sock1.connect(('localhost', 11111))

sock2 = socket.socket()
sock2.connect(('localhost', 22222))

sock1.send(b'Register')
sock2.send(b'Register')

sel = selectors.DefaultSelector() # 이벤트 처리기(셀렉터) 생성

# 서버 소켓(신규 클라이언트 연결을 처리하는 소켓)을 이벤트 처리기에 등록
sel.register(sock1, selectors.EVENT_READ, read1)
sel.register(sock2, selectors.EVENT_READ, read2)

while True:
    events = sel.select() # 등록된 객체에 대한 이벤트 감시 시작
    for key, mask in events: # 발생한 이벤트를 모두 검사
        callback = key.data # key.data: 이벤트 처리기에 등록한 callback 함수
        callback(key.fileobj, mask) # callback 함수 호출