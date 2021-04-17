from socket import *

BUFF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM) # IPv4, UDP
sock.bind(('', port))

message = {} # 메시지 박스 설정
while True:
    data, addr = sock.recvfrom(BUFF_SIZE) # client로부터 메시지 수신
    request = data.decode() # 수신한 메시지 encoding

    if request[:4] == 'send': # send 요청일 경우
        order = request[:4] # 명령어
        mboxId = request[5] # 메시지 박스 ID
        content = request[7:] # 메시지 내용

        if mboxId in message.keys(): # 메시지 박스에 이미 메시지 박스 ID가 있다면
            message[mboxId].append(content) # 해당 ID에 메시지 추가
        else:
            message[mboxId] = [content, ] # 메시지 박스 ID를 key로 하는 데이터 추가
        sock.sendto(b'OK', addr) # 모두 종료 후 client에게 OK 메시지 전송
    elif request[:4] == 'rece': # receive 요청일 경우
        try:
            msg = message[request[8]][0] # 가장 맨 앞 메시지 꺼내기
            del message[request[8]][0] # 가장 맨 앞 메시지 삭제
            sock.sendto(msg.encode(), addr) # 찾은 메시지를 전송
        except:
            sock.sendto(b'No messages', addr) # 메시지를 꺼내고 삭제하는 과정에서 오류 시 에러 메시지 전송
    elif request[:4] == 'quit': # quit 메시지 수신 후
        sock.close() # 소켓 종료
        break

    print(message)