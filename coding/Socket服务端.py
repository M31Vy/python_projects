import socket

socket_server = socket.socket()
socket_server.bind(('localhost', 8888))

socket_server.listen(1)

conn, address = socket_server.accept()
print(f'收到连接，客户端地址为：{address}')

while True:
    data: str = conn.recv(1024).decode('UTF-8')
    print(f'收到消息：{data}')
    if data in ('exit', '退出'):
        break

    msg = input('请输入回复的消息：')
    if msg in ('exit', '退出'):
        break

    conn.send(msg.encode('UTF-8'))

conn.close()
socket_server.close()