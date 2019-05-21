import socket


class ClientSend:
    def __init__(self, wizard="b", username="Bob"):
        self.w = wizard
        self.n = username

    def send(self,  xCoord=-20, yCoord=-20, level=0, mySocket=socket.socket()):
        mySocket.send(str([self.n, self.w,  xCoord, yCoord, level]).encode())


def main():
    host = '174.93.72.251'
    port = 8888

    mySocket = socket.socket()
    mySocket.connect((host, port))
    print("Connection Successful")
    client = ClientSend("Yep", "WAAAAAAAAAAAAAAAAAAAAAAAAAAH")
    while True:
        client.send(20, 61, 0, mySocket)
        data = mySocket.recv(1024).decode()
        print('Received from server: ' + data)
        end = input(">>")
        if end == "e":
            break

    mySocket.close()


main()
