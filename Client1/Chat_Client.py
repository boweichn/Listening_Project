import socket
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8081))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    userInput = input("Please send a message to receiver: \n")
    if userInput != 'quit':
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 8087))
        clientsocket.sendall(userInput.encode('utf-8'))
    else:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 8087))
        clientsocket.sendall(userInput.encode('utf-8'))
        break