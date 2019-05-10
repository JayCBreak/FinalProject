import socket

class ClientSend:
    def __init__(self, wizard = "b", username = "Bob", xCoord = 20, yCoord = 20):
        self.w = wizard
        self.n = username
        self.x = xCoord
        self.y = yCoord

    def send(self):
        message = [self.n, self.w, self.x., self.y]
        mySocket.send(message.encode()+"\n")
        data = mySocket.recv(1024).decode()

def main():
    host = '192.168.2.42'
    port = 8888

    mySocket = socket.socket()
    mySocket.connect((host, port))

    while True:


        print('Received from server: ' + data)

        message = input(" -> ")

    mySocket.close()


main()
