import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024) # server로부터 접속 정보 수신
print(msg.decode()) # 문자열을 decoding 후 출력

sock.send(b'Namjoon Lee') # server에게 영문 이름 encoding 후 송신

stu_num = sock.recv(1024) # server로부터 학번 수신
print(int.from_bytes(stu_num, 'big')) # 수신한 byte 객체를 정수로 변환 후 출력

sock.close()