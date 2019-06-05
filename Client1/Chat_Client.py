import socket
import pickle

class Server:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, listen_port=8081):
        self.listen_port = listen_port    # set port attribute

    def message_app(self):

        while True:
            userInput = input("Please send a message to receiver: \n")  # user input for message
            if userInput != 'quit':
                clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientsocket.connect(('localhost', 8087))               # connect to server
                clientsocket.send(userInput.encode('utf-8'))
            else:                                                       # quit when input is given
                clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientsocket.connect(('localhost', 8087))               #connect to server
                clientsocket.send(userInput.encode('utf-8'))
                break

if __name__ == "__main__":
    Server = Server()                                             # create instance
    Server.message_app()                                               # proc method