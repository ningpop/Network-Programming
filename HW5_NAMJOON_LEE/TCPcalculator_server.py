from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        try:
            temp = eval(data.decode()) # 데이터를 받아와 decoding 후 계산
            if isinstance(temp, float): # 계산한 값이 소수라면
                result = round(temp, 1) # 소수점 1자리까지만 표시
            else:
                result = temp

            print(f'data: {result}, data type: {type(result)}') # 서버측에서 만들어진 데이터 확인

        except: # error 발생 시 client에게 오류 메시지 전송
            client.send(b'Try again')
        else:
            client.send(str(result).encode()) # client에 계산 결과 encoding 후 전송
        
    client.close()