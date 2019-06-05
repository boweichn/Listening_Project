import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8087))
serversocket.listen(5) # become a server socket, maximum 5 connections

Client1_Port = 8081
Cleint2_Port = 8082

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    # buf_info = connection.getpeername() \ this is to get port for client info.
    if len(buf) > 0 and buf.decode("utf-8") != 'quit':
        print(buf.decode("utf-8"))
    elif buf.decode("utf-8") == 'quit':
        break
        