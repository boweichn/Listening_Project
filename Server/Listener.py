import socket
import threading


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8087))
serversocket.listen(5) # become a server socket, maximum 5 connections

Client1_Port = 8081
Cleint2_Port = 8082

# def receive_output(): 
#     while True:
#         connection, address = serversocket.accept()
#         buf = connection.recv(64)
#         # buf_info = connection.getpeername() \ this is to get port for client info.

#         test_input = input(str("enter something: \n"))

#         if len(buf) > 0 and buf.decode("utf-8") != 'quit':
#             print(buf.decode("utf-8"))
#         elif buf.decode("utf-8") == 'quit':
#             break

def test_input():
    while True:
        test = input("enter something\n")
        if test == 'quit':
            break
    return

def send_input():
    while True:
        userInput = input("Please send a message to receiver: \n")  # user input for message
        if userInput != 'quit':
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect(('localhost', Client1_Port))               # connect to server
            clientsocket.send(userInput.encode('utf-8'))
        else:                                                       # quit when input is given
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect(('localhost', Client1_Port))               #connect to server
            clientsocket.send(userInput.encode('utf-8'))

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      print_time(self.name, 5, self.counter)
      print "Exiting " + self.name

if __name__ == "__main__":
    