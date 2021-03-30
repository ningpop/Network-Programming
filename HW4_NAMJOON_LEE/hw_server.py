import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)

    client.send(b'Hello ' + addr[0].encode()) # client에게 접속 정보 송신

    print(client.recv(1024).decode()) # client로부터 영문 이름 수신해 decoding 후 출력

    client.send((20154015).to_bytes(4, 'big')) # client에게 학번 정수값을 변환(big endian) 후 송신

    client.close()