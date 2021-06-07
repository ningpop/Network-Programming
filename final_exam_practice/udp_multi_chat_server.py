import socket
import time

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 2500))

print('Server Started')

while True:
    data, addr = s.recvfrom(1024)
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove(addr)
            continue
    
    if addr not in clients:
        print('new client', addr)
        clients.append(addr)

    print(time.asctime() + str(addr) + ':' + data.decode())

    for client in clients:
        if client != addr:
            s.sendto(data, client)