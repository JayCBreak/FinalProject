import socket


class ClientSend:
    def __init__(self, wizard="b", username="Bob"):
        self.w = wizard
        self.n = username
        self.h = "174.93.72.251"
        self.p = 8888

    def send(self,  xCoord=-20, yCoord=-20, level=0, mySocket=socket.socket()):
        mySocket.send(str([self.n, self.w,  xCoord, yCoord, level]).encode())


def main():
    host = '174.93.72.251'
    port = 8888

    mySocket = socket.socket()
    mySocket.connect((host, port))
    print("Connection Successful")
    client = ClientSend("y", "I AM not GOD hehe")
    while True:
        client.send(20, 61, 0, mySocket)
        data = mySocket.recv(1024).decode()
        print('Received from server: ' + data)
        #end = input(">>")
        #if end == "e":
         #   break

    mySocket.close()


main()
