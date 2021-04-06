from socket import *

s = socket(AF_INET, SOCK_STREAM) # IPv4, TCP
s.bind(('', 80)) # HTTP에 사용되는 80 port로 binding
s.listen(10) # 최대 접속 소켓 수 10
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)

    data = client.recv(1024) # 최대 수신 1024 Bytes
    msg = data.decode()
    req = msg.split('\r\n') # \r\n을 기준으로 client의 request 문자열을 split

    request = req[0].split() # request header의 첫 문장을 split. 여기서 req[0]는 GET /index.html HTTP/1.1
    request_method = request[0] # HTTP request method (ex. GET, POST...)
    filename = request[1].lstrip('/') # request file name without '/'

    if filename == '':
        filename = 'index.html' # 127.0.0.1로만 접속 시에도 메인 페이지 연결
    print(request_method, filename)

    try:
        if filename.endswith('.html'): # request file이 html 파일이라면
            f = open(filename, 'r', encoding='utf-8') # file open
            data = f.read() # file read

            mimeType = 'text/html'
            header = 'HTTP/1.1 200 OK\r\n' + mimeType + '\r\n' + '\r\n' # mimeType과 함께 header 생성

            client.send(header.encode('utf-8')) # header encoding 후 전송
            client.send(data.encode('euc-kr')) # 한글이 포함된 html 본문을 euc-kr로 encoding 후 전송
            f.close() # file close

        elif filename.endswith('.png'): # request file이 png 파일이라면
            f = open('iot.png', 'rb') # file open
            data = f.read() # file read

            mimeType = 'image/png'
            header = 'HTTP/1.1 200 OK\r\n' + mimeType + '\r\n' + '\r\n' # mimeType과 함께 header 생성

            client.send(header.encode('utf-8')) # header encoding 후 전송
            client.send(data) # request된 png 파일을 전송 (image 파일 자체를 binary로 열었으므로 그대로 전송)
            f.close()

        elif filename.endswith('.ico'): # request file이 ico 파일이라면
            f = open('favicon.ico', 'rb') # file open
            data = f.read() # file read

            mimeType = 'image/x-icon'
            header = 'HTTP/1.1 200 OK\r\n' + mimeType + '\r\n' + '\r\n' # mimeType과 함께 header 생성

            client.send(header.encode('utf-8')) # header encoding 후 전송
            client.send(data) # request된 ico 파일을 전송 (image 파일 자체를 binary로 열었으므로 그대로 전송)
            f.close()
        
        else: # 그 외 요청이 들어왔을 시
            raise Exception # 예외 발생

    except Exception as e:
        mimeType = 'text/html'
        header = 'HTTP/1.1 404 Not Found\r\n' + mimeType + '\r\n' + '\r\n' # mimeType과 함께 Not Found header 생성

        response = '<html><head><title>Not Found</title></head><body>Not Found</body></html>' # 그 외의 요청시 응답할 Not Found html 본문

        client.send(header.encode('utf-8')) # header encoding 후 전송
        client.send(response.encode('utf-8')) # Not Found 응답 본문을 encoding 후 전송

    client.close()